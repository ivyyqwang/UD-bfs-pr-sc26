/*
 * scc.c - High-performance Strongly Connected Components (Tarjan's Algorithm)
 *
 * Designed for Stanford Large Network Dataset Collection (SNAP) graphs.
 * Input format: edge-list text files (comment lines starting with '#')
 *
 * Compile:
 *   gcc -O3 -march=native -o scc scc.c
 *
 * Usage:
 *   ./scc <graph_file.txt>
 *
 * Example (SNAP dataset):
 *   ./scc web-Google.txt
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

/* -------------------------------------------------------------------------
 * Timing helpers
 * ------------------------------------------------------------------------- */
static inline double now_sec(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}

/* -------------------------------------------------------------------------
 * CSR graph representation
 * ------------------------------------------------------------------------- */
typedef struct {
    uint32_t  n;          /* number of vertices                   */
    uint64_t  m;          /* number of edges                      */
    uint64_t *row_ptr;    /* row_ptr[v] .. row_ptr[v+1]-1 = neighbours of v */
    uint32_t *col_idx;    /* destination vertices                  */
} Graph;

/* -------------------------------------------------------------------------
 * Edge list (used during ingestion only)
 * ------------------------------------------------------------------------- */
typedef struct { uint32_t src, dst; } Edge;

/* -------------------------------------------------------------------------
 * Graph ingestion
 * Returns elapsed ingestion time (excluded from SCC perf metrics).
 * ------------------------------------------------------------------------- */
static Graph *load_graph(const char *path, double *ingest_time) {
    double t0 = now_sec();

    FILE *f = fopen(path, "r");
    if (!f) { perror("fopen"); exit(1); }

    /* ---- first pass: count edges & find max node id ---- */
    uint64_t edge_cap = 1 << 20;
    Edge    *edges    = (Edge *)malloc(edge_cap * sizeof(Edge));
    if (!edges) { fprintf(stderr, "OOM\n"); exit(1); }

    uint64_t m   = 0;
    uint32_t max_id = 0;
    char     line[256];

    while (fgets(line, sizeof(line), f)) {
        if (line[0] == '#' || line[0] == '\n') continue;
        uint32_t u, v;
        if (sscanf(line, "%u %u", &u, &v) != 2) continue;
        if (m == edge_cap) {
            edge_cap *= 2;
            edges = (Edge *)realloc(edges, edge_cap * sizeof(Edge));
            if (!edges) { fprintf(stderr, "OOM\n"); exit(1); }
        }
        edges[m].src = u;
        edges[m].dst = v;
        m++;
        if (u > max_id) max_id = u;
        if (v > max_id) max_id = v;
    }
    fclose(f);

    uint32_t n = max_id + 1;

    /* ---- build CSR ---- */
    Graph *g      = (Graph *)malloc(sizeof(Graph));
    g->n          = n;
    g->m          = m;
    g->row_ptr    = (uint64_t *)calloc((uint64_t)(n + 1), sizeof(uint64_t));
    g->col_idx    = (uint32_t *)malloc(m * sizeof(uint32_t));
    if (!g->row_ptr || !g->col_idx) { fprintf(stderr, "OOM\n"); exit(1); }

    /* count out-degrees */
    for (uint64_t i = 0; i < m; i++) g->row_ptr[edges[i].src + 1]++;
    /* prefix sum */
    for (uint32_t i = 1; i <= n; i++) g->row_ptr[i] += g->row_ptr[i - 1];
    /* fill col_idx */
    uint64_t *tmp = (uint64_t *)malloc((uint64_t)(n) * sizeof(uint64_t));
    if (!tmp) { fprintf(stderr, "OOM\n"); exit(1); }
    memcpy(tmp, g->row_ptr, (uint64_t)n * sizeof(uint64_t));
    for (uint64_t i = 0; i < m; i++) {
        uint32_t s = edges[i].src;
        g->col_idx[tmp[s]++] = edges[i].dst;
    }
    free(tmp);
    free(edges);

    *ingest_time = now_sec() - t0;
    return g;
}

/* -------------------------------------------------------------------------
 * Iterative Tarjan's SCC
 *
 * Classic recursive Tarjan's overflows the C stack on large graphs.
 * We simulate the DFS stack explicitly.
 *
 * State per node (packed to reduce cache pressure):
 *   index    – discovery order  (UINT32_MAX = unvisited)
 *   lowlink  – lowest reachable index
 *   on_stack – bool
 * ------------------------------------------------------------------------- */

#define UNVISITED UINT32_MAX

typedef struct {
    uint32_t node;    /* vertex being processed           */
    uint64_t edge;    /* next edge index to explore       */
} Frame;

typedef struct {
    uint32_t *comp;       /* comp[v] = SCC id for vertex v   */
    uint32_t  num_scc;    /* total SCCs found                */
    uint64_t  edges_traversed; /* total edge traversals       */
} SCCResult;

static SCCResult *tarjan_scc(const Graph *g) {
    uint32_t n = g->n;

    uint32_t *index   = (uint32_t *)malloc((uint64_t)n * sizeof(uint32_t));
    uint32_t *lowlink = (uint32_t *)malloc((uint64_t)n * sizeof(uint32_t));
    uint8_t  *on_stk  = (uint8_t  *)calloc((uint64_t)n, 1);
    uint32_t *comp    = (uint32_t *)malloc((uint64_t)n * sizeof(uint32_t));

    /* Tarjan node stack */
    uint32_t *node_stack     = (uint32_t *)malloc((uint64_t)n * sizeof(uint32_t));
    uint32_t  node_stack_top = 0;

    /* DFS call stack */
    Frame    *call_stack     = (Frame    *)malloc((uint64_t)n * sizeof(Frame));
    uint32_t  call_top       = 0;

    if (!index || !lowlink || !on_stk || !comp || !node_stack || !call_stack) {
        fprintf(stderr, "OOM in Tarjan\n"); exit(1);
    }

    memset(index, 0xFF, (uint64_t)n * sizeof(uint32_t)); /* UNVISITED */

    uint32_t  timer        = 0;
    uint32_t  num_scc      = 0;
    uint64_t  edges_done   = 0;

    for (uint32_t start = 0; start < n; start++) {
        if (index[start] != UNVISITED) continue;

        /* push initial frame */
        call_stack[0].node = start;
        call_stack[0].edge = g->row_ptr[start];
        call_top           = 1;

        index[start]   = lowlink[start] = timer++;
        on_stk[start]  = 1;
        node_stack[node_stack_top++] = start;

        while (call_top > 0) {
            Frame *fr = &call_stack[call_top - 1];
            uint32_t u = fr->node;
            uint64_t end = g->row_ptr[u + 1];

            if (fr->edge < end) {
                uint32_t v = g->col_idx[fr->edge];
                fr->edge++;
                edges_done++;

                if (index[v] == UNVISITED) {
                    /* tree edge: recurse */
                    index[v] = lowlink[v] = timer++;
                    on_stk[v] = 1;
                    node_stack[node_stack_top++] = v;

                    call_stack[call_top].node = v;
                    call_stack[call_top].edge = g->row_ptr[v];
                    call_top++;
                } else if (on_stk[v]) {
                    /* back edge */
                    if (lowlink[v] < lowlink[u]) lowlink[u] = lowlink[v];
                }
            } else {
                /* all neighbours processed – pop frame */
                call_top--;

                if (call_top > 0) {
                    uint32_t parent = call_stack[call_top - 1].node;
                    if (lowlink[u] < lowlink[parent]) lowlink[parent] = lowlink[u];
                }

                /* root of an SCC? */
                if (lowlink[u] == index[u]) {
                    while (1) {
                        uint32_t w = node_stack[--node_stack_top];
                        on_stk[w] = 0;
                        comp[w]   = num_scc;
                        if (w == u) break;
                    }
                    num_scc++;
                }
            }
        }
    }

    free(index); free(lowlink); free(on_stk);
    free(node_stack); free(call_stack);

    SCCResult *res = (SCCResult *)malloc(sizeof(SCCResult));
    res->comp           = comp;
    res->num_scc        = num_scc;
    res->edges_traversed = edges_done;
    return res;
}

/* -------------------------------------------------------------------------
 * Statistics helpers
 * ------------------------------------------------------------------------- */
static void print_scc_stats(const SCCResult *res, uint32_t n) {
    /* count SCC sizes */
    uint32_t *sizes = (uint32_t *)calloc(res->num_scc, sizeof(uint32_t));
    for (uint32_t v = 0; v < n; v++) sizes[res->comp[v]]++;

    uint32_t max_size = 0;
    uint32_t trivial  = 0;   /* size == 1 */
    for (uint32_t i = 0; i < res->num_scc; i++) {
        if (sizes[i] > max_size) max_size = sizes[i];
        if (sizes[i] == 1)       trivial++;
    }
    free(sizes);

    printf("  Total SCCs found   : %u\n",  res->num_scc);
    printf("  Largest SCC size   : %u\n",  max_size);
    printf("  Trivial SCCs (size=1): %u\n", trivial);
    printf("  Non-trivial SCCs   : %u\n",  res->num_scc - trivial);
}

/* -------------------------------------------------------------------------
 * main
 * ------------------------------------------------------------------------- */
int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <snap_graph_file>\n", argv[0]);
        return 1;
    }

    printf("=== SCC (Tarjan, iterative) ===\n\n");
    printf("Input file : %s\n", argv[1]);

    /* ---- ingestion (not counted in perf metric) ---- */
    double ingest_sec;
    Graph *g = load_graph(argv[1], &ingest_sec);

    printf("Graph      : %u vertices, %llu edges\n", g->n, (unsigned long long)g->m);
    printf("Ingest time: %.3f s  (excluded from SCC metrics)\n\n", ingest_sec);

    /* ---- SCC computation ---- */
    double t0  = now_sec();
    SCCResult *res = tarjan_scc(g);
    double elapsed = now_sec() - t0;

    double teps = (elapsed > 0) ? (double)res->edges_traversed / elapsed : 0.0;

    printf("--- Performance ---\n");
    printf("  SCC wall time      : %.6f s\n",   elapsed);
    printf("  Edges traversed    : %llu\n",      (unsigned long long)res->edges_traversed);
    printf("  Throughput         : %.3f M edges/s\n", teps / 1e6);

    printf("\n--- SCC Statistics ---\n");
    print_scc_stats(res, g->n);

    /* cleanup */
    free(res->comp);
    free(res);
    free(g->row_ptr);
    free(g->col_idx);
    free(g);

    return 0;
}
