/*
 * kcore.c — K-Core Decomposition for SNAP-format graphs
 *
 * Supports edge-list files from the Stanford Large Network Dataset Collection
 * (https://snap.stanford.edu/data/).  Lines beginning with '#' are treated as
 * comments and skipped.  Both directed and undirected edge-lists work; each
 * directed edge (u,v) is stored as an undirected edge.
 *
 * Algorithm: O(m) peeling via a degree-bucket queue (Batagelj & Zaversnik 2003)
 *
 * Build:
 *   gcc -O3 -march=native -o kcore kcore.c
 *
 * Usage:
 *   ./kcore <edge-list-file>          # decompose whole graph
 *   ./kcore <edge-list-file> <k>      # only show nodes with core number >= k
 *
 * Output:
 *   - Core-number distribution summary
 *   - Per-run performance: elapsed wall time, edges traversed, MTEPS
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>
#include <inttypes.h>

/* --------------------------------------------------------------------------
 * Timing helper (POSIX clock_gettime, falls back to clock() on Windows)
 * -------------------------------------------------------------------------- */
static double now_seconds(void) {
#if defined(_POSIX_TIMERS) && _POSIX_TIMERS > 0
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
#else
    return (double)clock() / CLOCKS_PER_SEC;
#endif
}

/* --------------------------------------------------------------------------
 * Graph storage (CSR — Compressed Sparse Row)
 * -------------------------------------------------------------------------- */
typedef struct {
    uint32_t  n;          /* number of vertices (0 … n-1)            */
    uint64_t  m;          /* number of undirected edges               */
    uint32_t *deg;        /* deg[v]  = degree of v                    */
    uint32_t *xadj;       /* xadj[v] = start of v's neighbour list   */
    uint32_t *adj;        /* adj[xadj[v]…xadj[v+1]-1] = neighbours  */
} Graph;

/* --------------------------------------------------------------------------
 * Edge buffer used during ingestion
 * -------------------------------------------------------------------------- */
typedef struct { uint32_t u, v; } Edge;

static void graph_free(Graph *g) {
    free(g->deg);
    free(g->xadj);
    free(g->adj);
}

/* --------------------------------------------------------------------------
 * Load a SNAP edge-list file and build a CSR graph.
 * Returns 0 on success, non-zero on error.
 * -------------------------------------------------------------------------- */
static int load_graph(const char *path, Graph *g) {
    FILE *fp = fopen(path, "r");
    if (!fp) { perror("fopen"); return 1; }

    /* --- first pass: collect edges ---------------------------------------- */
    size_t  cap   = 1 << 20;
    size_t  ecnt  = 0;
    Edge   *edges = (Edge *)malloc(cap * sizeof(Edge));
    if (!edges) { fclose(fp); return 1; }

    uint32_t max_node = 0;
    char line[256];

    while (fgets(line, sizeof(line), fp)) {
        if (line[0] == '#' || line[0] == '%' || line[0] == '\n') continue;

        uint32_t u, v;
        if (sscanf(line, "%" SCNu32 " %" SCNu32, &u, &v) != 2) continue;
        if (u == v) continue;          /* skip self-loops */

        if (ecnt == cap) {
            cap *= 2;
            Edge *tmp = (Edge *)realloc(edges, cap * sizeof(Edge));
            if (!tmp) { free(edges); fclose(fp); return 1; }
            edges = tmp;
        }
        edges[ecnt].u = u;
        edges[ecnt].v = v;
        ecnt++;

        if (u > max_node) max_node = u;
        if (v > max_node) max_node = v;
    }
    fclose(fp);

    uint32_t n = max_node + 1;

    /* --- count degrees (treat each directed edge as undirected) ------------ */
    uint32_t *deg = (uint32_t *)calloc(n, sizeof(uint32_t));
    if (!deg) { free(edges); return 1; }

    for (size_t i = 0; i < ecnt; i++) {
        deg[edges[i].u]++;
        deg[edges[i].v]++;
    }

    /* --- build xadj -------------------------------------------------------- */
    uint32_t *xadj = (uint32_t *)malloc((n + 1) * sizeof(uint32_t));
    if (!xadj) { free(deg); free(edges); return 1; }

    xadj[0] = 0;
    for (uint32_t i = 0; i < n; i++) xadj[i + 1] = xadj[i] + deg[i];

    uint64_t total_adj = xadj[n];   /* = 2 * number of undirected edges */

    uint32_t *adj = (uint32_t *)malloc(total_adj * sizeof(uint32_t));
    if (!adj) { free(xadj); free(deg); free(edges); return 1; }

    /* --- fill adjacency list ----------------------------------------------- */
    uint32_t *pos = (uint32_t *)calloc(n, sizeof(uint32_t));
    if (!pos) { free(adj); free(xadj); free(deg); free(edges); return 1; }

    for (size_t i = 0; i < ecnt; i++) {
        uint32_t u = edges[i].u, v = edges[i].v;
        adj[xadj[u] + pos[u]++] = v;
        adj[xadj[v] + pos[v]++] = u;
    }
    free(pos);
    free(edges);

    g->n    = n;
    g->m    = ecnt;          /* number of unique (directed) input edges */
    g->deg  = deg;
    g->xadj = xadj;
    g->adj  = adj;
    return 0;
}

/* --------------------------------------------------------------------------
 * K-Core decomposition  (Batagelj & Zaversnik, 2003)
 *
 * Returns an array core[0..n-1] with the core number of each vertex, and
 * stores the number of edge-endpoint visits in *edges_traversed.
 * -------------------------------------------------------------------------- */
static uint32_t *kcore_decompose(const Graph *g, uint64_t *edges_traversed) {
    uint32_t  n    = g->n;
    uint32_t *core = (uint32_t *)malloc(n * sizeof(uint32_t));
    uint32_t *wd   = (uint32_t *)malloc(n * sizeof(uint32_t)); /* working degree */
    if (!core || !wd) { free(core); free(wd); return NULL; }

    /* copy degrees into working array */
    uint32_t max_deg = 0;
    for (uint32_t v = 0; v < n; v++) {
        wd[v] = g->deg[v];
        if (wd[v] > max_deg) max_deg = wd[v];
    }

    /* --- bucket sort by degree -------------------------------------------- */
    uint32_t *bin   = (uint32_t *)calloc(max_deg + 1, sizeof(uint32_t));
    uint32_t *pos   = (uint32_t *)malloc(n * sizeof(uint32_t));
    uint32_t *order = (uint32_t *)malloc(n * sizeof(uint32_t));
    if (!bin || !pos || !order) {
        free(bin); free(pos); free(order); free(core); free(wd);
        return NULL;
    }

    for (uint32_t v = 0; v < n; v++) bin[wd[v]]++;

    uint32_t start = 0;
    for (uint32_t d = 0; d <= max_deg; d++) {
        uint32_t cnt = bin[d];
        bin[d] = start;
        start += cnt;
    }

    for (uint32_t v = 0; v < n; v++) {
        pos[v]         = bin[wd[v]];
        order[pos[v]]  = v;
        bin[wd[v]]++;
    }

    /* restore bin[d] to point to the first vertex of degree d */
    for (uint32_t d = max_deg; d > 0; d--) bin[d] = bin[d - 1];
    bin[0] = 0;

    /* --- peeling ---------------------------------------------------------- */
    uint64_t et = 0;   /* edge traversals counter */

    for (uint32_t i = 0; i < n; i++) {
        uint32_t v = order[i];
        core[v] = wd[v];

        uint32_t start_v = g->xadj[v];
        uint32_t end_v   = g->xadj[v + 1];

        for (uint32_t j = start_v; j < end_v; j++) {
            et++;
            uint32_t u = g->adj[j];

            if (wd[u] > wd[v]) {
                /* move u one step earlier inside its bucket */
                uint32_t du   = wd[u];
                uint32_t pu   = pos[u];
                uint32_t pw   = bin[du];   /* first position of bucket du */
                uint32_t w    = order[pw]; /* vertex currently at that position */

                if (u != w) {
                    /* swap u and w */
                    pos[u]    = pw;
                    pos[w]    = pu;
                    order[pu] = w;
                    order[pw] = u;
                }
                bin[du]++;
                wd[u]--;
            }
        }
    }

    *edges_traversed = et;
    free(bin);
    free(pos);
    free(order);
    free(wd);
    return core;
}

/* --------------------------------------------------------------------------
 * Print distribution of core numbers
 * -------------------------------------------------------------------------- */
static void print_core_stats(const uint32_t *core, uint32_t n, int min_k) {
    uint32_t max_core = 0;
    for (uint32_t v = 0; v < n; v++)
        if (core[v] > max_core) max_core = core[v];

    uint64_t *freq = (uint64_t *)calloc(max_core + 1, sizeof(uint64_t));
    if (!freq) return;
    for (uint32_t v = 0; v < n; v++) freq[core[v]]++;

    printf("\n=== Core-number distribution ===\n");
    printf("  %-12s  %s\n", "core k", "# vertices");
    printf("  %-12s  %s\n", "------", "----------");

    uint64_t cumulative = 0;
    for (uint32_t k = (uint32_t)(min_k > 0 ? min_k : 0); k <= max_core; k++) {
        if (freq[k] > 0) {
            cumulative += freq[k];
            printf("  %-12" PRIu32 "  %" PRIu64 "\n", k, freq[k]);
        }
    }

    printf("\nMaximum core number  : %" PRIu32 "\n", max_core);
    printf("Total nodes reported : %" PRIu64 "\n", cumulative);
    free(freq);
}

/* --------------------------------------------------------------------------
 * main
 * -------------------------------------------------------------------------- */
int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr,
            "Usage: %s <snap-edge-list> [min_k]\n\n"
            "  snap-edge-list  Path to a SNAP .txt edge-list file\n"
            "  min_k           Optional: only display cores >= min_k\n\n"
            "Example:\n"
            "  %s roadNet-CA.txt\n"
            "  %s com-dblp.ungraph.txt 5\n",
            argv[0], argv[0], argv[0]);
        return 1;
    }

    const char *path  = argv[1];
    int         min_k = (argc >= 3) ? atoi(argv[2]) : 0;

    /* -----------------------------------------------------------------------
     * Ingestion  (NOT counted in performance metric)
     * --------------------------------------------------------------------- */
    printf("Loading graph from: %s\n", path);
    double t_load_start = now_seconds();

    Graph g;
    memset(&g, 0, sizeof(g));
    if (load_graph(path, &g) != 0) {
        fprintf(stderr, "Failed to load graph.\n");
        return 1;
    }

    double t_load_end = now_seconds();

    /* undirected edge count = half the adjacency list entries */
    uint64_t undirected_edges = g.xadj[g.n] / 2;

    printf("Graph loaded in %.3f s\n", t_load_end - t_load_start);
    printf("Vertices : %" PRIu32 "\n", g.n);
    printf("Edges    : %" PRIu64 "  (undirected)\n", undirected_edges);

    /* -----------------------------------------------------------------------
     * K-Core decomposition  (performance metric starts HERE)
     * --------------------------------------------------------------------- */
    printf("\nRunning k-core decomposition ...\n");

    uint64_t edges_traversed = 0;
    double   t_start         = now_seconds();

    uint32_t *core = kcore_decompose(&g, &edges_traversed);

    double t_end = now_seconds();
    /* performance metric ends HERE */

    if (!core) {
        fprintf(stderr, "k-core decomposition failed (out of memory?).\n");
        graph_free(&g);
        return 1;
    }

    double elapsed = t_end - t_start;

    /* -----------------------------------------------------------------------
     * Performance statistics
     * --------------------------------------------------------------------- */
    printf("\n=== Performance Statistics ===\n");
    printf("  Wall-clock time        : %.6f s\n",  elapsed);
    printf("  Edges traversed        : %" PRIu64 "\n", edges_traversed);

    if (elapsed > 0.0) {
        double mteps = (double)edges_traversed / elapsed / 1e6;
        printf("  Throughput             : %.2f MTEPS  (mega edge-traversals/s)\n",
               mteps);
        printf("  Edges/second           : %.0f\n",
               (double)edges_traversed / elapsed);
    } else {
        printf("  Throughput             : (elapsed time too small to measure)\n");
    }

    /* -----------------------------------------------------------------------
     * Core-number statistics
     * --------------------------------------------------------------------- */
    print_core_stats(core, g.n, min_k);

    free(core);
    graph_free(&g);
    return 0;
}
