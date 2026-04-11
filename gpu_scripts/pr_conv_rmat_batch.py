import os
import sys
import time

import cugraph
import cudf
import numpy as np
import cupy.cuda.nvtx as nvtx
from cugraph.generators import rmat


def generate_rmat_graph(scale, edge_factor, a=0.57, b=0.19, c=0.19, seed=0):
    num_edges = edge_factor * (2 ** scale)
    G = rmat(
        scale,
        num_edges,
        a=a,
        b=b,
        c=c,
        seed=seed,
        clip_and_flip=False,
        scramble_vertex_ids=False,
    )

    edge_df = G.view_edge_list()
    edge_df["src"] = edge_df["src"].astype("int64")
    edge_df["dst"] = edge_df["dst"].astype("int64")
    if "edge_id" in edge_df.columns:
        edge_df["edge_id"] = edge_df["edge_id"].astype("int64")

    # PageRank expects weighted edges here, so assign a uniform weight.
    edge_df["weight"] = np.float64(1.0)

    G64 = cugraph.Graph(directed=False)
    G64.from_cudf_edgelist(
        edge_df,
        source="src",
        destination="dst",
        edge_attr="weight",
        store_transposed=True,
    )

    return G64


def parse_rmat_params_file(list_file_path):
    if not os.path.isfile(list_file_path):
        raise FileNotFoundError(f"RMAT params file not found: {list_file_path}")

    rmat_params = []
    with open(list_file_path, "r") as f:
        for line_num, raw_line in enumerate(f, start=1):
            line = raw_line.strip()

            if not line or line.startswith("#"):
                continue

            parts = [part.strip() for part in line.split(",")]
            if len(parts) != 2:
                raise ValueError(
                    f"Invalid format at line {line_num} in {list_file_path}. "
                    "Expected: scale, edge_factor"
                )

            try:
                scale = int(parts[0])
            except ValueError as exc:
                raise ValueError(
                    f"Invalid scale at line {line_num} in {list_file_path}: {parts[0]}"
                ) from exc

            try:
                edge_factor = int(parts[1])
            except ValueError as exc:
                raise ValueError(
                    f"Invalid edge_factor at line {line_num} in {list_file_path}: {parts[1]}"
                ) from exc

            rmat_params.append((scale, edge_factor))

    if not rmat_params:
        raise ValueError(
            f"No valid scale,edge_factor entries found in file: {list_file_path}"
        )

    return rmat_params


def run_pr_once(
    scale,
    edge_factor,
    max_iter,
    alpha=0.85,
    tol=1e-6,
    warmup_iter=2,
    test_iter=5,
):
    G = generate_rmat_graph(scale, edge_factor)

    edge_list_df = G.view_edge_list()
    print(f"Vertex ID types: src={edge_list_df['src'].dtype}, dst={edge_list_df['dst'].dtype}")

    num_vertices = G.number_of_vertices()
    tol = np.float64(1.0 / num_vertices)
    initial_value = (1.0 - alpha) / num_vertices
    print("Number of vertices:", num_vertices)
    print("Number of edges:", G.number_of_edges())
    print("PageRank alpha:", alpha)
    print("PageRank initial value:", initial_value)
    print("PageRank max_iter:", max_iter)
    print("PageRank tolerance:", tol)

    num_vertices = G.number_of_vertices()
    if num_vertices == 0:
        raise ValueError("Input graph has no vertices")

    initial_value = (1.0 - alpha) / num_vertices
    nstart = cudf.DataFrame(
        {
            "vertex": G.nodes().astype(np.int64),
            "values": np.float64(initial_value),
        }
    )

    for _ in range(warmup_iter):
        _ = cugraph.pagerank(
            G,
            alpha=alpha,
            max_iter=max_iter,
            tol=tol,
            nstart=nstart,
            fail_on_nonconvergence=False,
        )

    t_total = 0.0
    for i in range(test_iter):
        t0 = time.perf_counter()
        if i == 0:
            nvtx.RangePush("pagerank")
        _pr_result, converged = cugraph.pagerank(
            G,
            alpha=alpha,
            max_iter=max_iter,
            tol=tol,
            nstart=nstart,
            fail_on_nonconvergence=False,
        )
        t1 = time.perf_counter()
        if i == 0:
            nvtx.RangePop()
        t_total += t1 - t0

    print("PageRank complete. Converged:", converged)
    print(f"Avg Processing Time: {t_total / test_iter * 1000:.4f} ms.")


def main():
    if len(sys.argv) != 2:
        print("Usage:")
        print("  python pr_rmat_batch.py <rmat_params_file>")
        print("Example:")
        print("  python pr_rmat_batch.py rmat_pr_list.txt")
        print("  # where each row is: scale, edge_factor, max_iter")
        print("  # scale: log2 of the number of vertices (e.g. 20 -> ~1M vertices)")
        print("  # edge_factor: num_edges = edge_factor * 2^scale (e.g. 16)")
        print("  # max_iter: PageRank max iterations")
        sys.exit(1)

    list_file = sys.argv[1]

    try:
        rmat_params = parse_rmat_params_file(list_file)
    except (ValueError, FileNotFoundError) as exc:
        print(f"Argument error: {exc}")
        sys.exit(1)

    for idx, (scale, edge_factor) in enumerate(rmat_params, start=1):
        print("\n" + "=" * 72)
        print(
            f"[{idx}/{len(rmat_params)}] scale={scale}, edge_factor={edge_factor}"
        )

        try:
            run_pr_once(scale, edge_factor, 2000)
        except Exception as exc:
            print(
                f"Failed for scale={scale}, edge_factor={edge_factor}, "
                f"max_iter={2000}: {exc}"
            )


if __name__ == "__main__":
    main()
