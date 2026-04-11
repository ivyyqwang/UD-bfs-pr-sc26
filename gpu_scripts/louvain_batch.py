import os
import sys
import time

import cugraph
import cudf
import numpy as np
import cupy.cuda.nvtx as nvtx


def load_tsv_to_cugraph(tsv_path, directed=False):
    with open(tsv_path, "r") as file:
        first_data_line = None
        for line in file:
            stripped = line.strip()
            if stripped:
                first_data_line = stripped
                break

    if first_data_line is None:
        raise ValueError(f"Input TSV file is empty: {tsv_path}")

    num_fields = len(first_data_line.split("\t"))

    if num_fields >= 3:
        df = cudf.read_csv(
            tsv_path,
            sep="\t",
            header=None,
            usecols=[0, 1, 2],
            names=["src", "dst", "weight"],
            dtype={"src": np.int64, "dst": np.int64, "weight": np.float64},
        )
    else:
        df = cudf.read_csv(
            tsv_path,
            sep="\t",
            header=None,
            usecols=[0, 1],
            names=["src", "dst"],
            dtype={"src": np.int64, "dst": np.int64},
        )

    print(f"Loaded edge rows: {len(df)}")

    G = cugraph.Graph(directed=directed)
    if "weight" in df.columns:
        G.from_cudf_edgelist(df, source="src", destination="dst", edge_attr="weight")
    else:
        G.from_cudf_edgelist(df, source="src", destination="dst")

    # edge_df = G.view_edge_list()
    # print(f"Vertex ID types: src={edge_df['src'].dtype}, dst={edge_df['dst'].dtype}")
    # if "weight" in df.columns:
    #     print(f"Edge weight type: {edge_df['weight'].dtype}")

    return G

def load_txt_to_cugraph(graph_path, directed=False):
    with open(graph_path, "r") as file:
        first_data_line = None
        for line in file:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                first_data_line = stripped
                break

    if first_data_line is None:
        raise ValueError(f"Input TXT file has no data rows: {graph_path}")

    preferred_sep = "\t" if "\t" in first_data_line else " "

    df = cudf.read_csv(
        graph_path,
        sep=preferred_sep,
        comment="#",
        header=None,
        usecols=[0, 1],
        names=["src", "dst"],
        dtype={"src": np.int64, "dst": np.int64},
        skipinitialspace=True,
    )
    

    print(f"Loaded edge rows: {len(df)}")

    G = cugraph.Graph(directed=directed)
    if "weight" in df.columns:
        G.from_cudf_edgelist(df, source="src", destination="dst", edge_attr="weight")
    else:
        G.from_cudf_edgelist(df, source="src", destination="dst")

    return G

def resolve_graph_path(graph_dir, graph_name):
    candidate = os.path.join(graph_dir, graph_name)
    if os.path.isfile(candidate):
        _, ext = os.path.splitext(candidate)
        ext = ext.lower()
        if ext == ".txt":
            return candidate, "txt"
        if ext == ".mtx":
            return candidate, "mtx"
        return candidate, "tsv"

    candidate_tsv = candidate + ".tsv"
    if os.path.isfile(candidate_tsv):
        return candidate_tsv, "tsv"

    candidate_txt = candidate + ".txt"
    if os.path.isfile(candidate_txt):
        return candidate_txt, "txt"

    candidate_mtx = candidate + ".mtx"
    if os.path.isfile(candidate_mtx):
        return candidate_mtx, "mtx"

    raise FileNotFoundError(
        f"Could not find graph file for '{graph_name}' in '{graph_dir}'. "
        "Tried raw name and .tsv/.txt/.mtx extensions."
    )



def parse_graph_k_pairs(args):
    if len(args) == 0 or len(args) % 2 != 0:
        raise ValueError("Graph/K arguments must be provided as pairs: <graph_name> <k> ...")

    pairs = []
    for i in range(0, len(args), 2):
        graph_name = args[i]
        k_value = int(args[i + 1])
        pairs.append((graph_name, k_value))
    return pairs


def parse_graph_k_file(list_file_path):
    if not os.path.isfile(list_file_path):
        raise FileNotFoundError(f"Graph list file not found: {list_file_path}")

    pairs = []
    with open(list_file_path, "r") as f:
        for line_num, raw_line in enumerate(f, start=1):
            line = raw_line.strip()

            if not line or line.startswith("#"):
                continue

            parts = [part.strip() for part in line.split(",")]
            if len(parts) != 2:
                raise ValueError(
                    f"Invalid format at line {line_num} in {list_file_path}. "
                    "Expected: graph_name, k_value"
                )

            graph_name = parts[0]
            try:
                k_value = int(parts[1])
            except ValueError as exc:
                raise ValueError(
                    f"Invalid k_value at line {line_num} in {list_file_path}: {parts[1]}"
                ) from exc

            pairs.append((graph_name, k_value))

    if not pairs:
        raise ValueError(f"No valid graph,k entries found in file: {list_file_path}")

    return pairs


def run_louvain_once(graph_file, graph_format, warmup_iter=2, test_iter=5):
    if graph_format == "txt":
        G = load_txt_to_cugraph(graph_file)
    elif graph_format == "mtx":
        G = load_mtx_to_cugraph(graph_file)
    else:
        G = load_tsv_to_cugraph(graph_file)

    print("Number of vertices:", G.number_of_vertices())
    print("Number of edges:", G.number_of_edges())

    for _ in range(warmup_iter):
        parts_df, modularity_score = cugraph.louvain(G)

    t_total = 0.0
    for i in range(test_iter):
        t0 = time.perf_counter()
        if i == 0:
            nvtx.RangePush("louvain")
        parts_df, modularity_score = cugraph.louvain(G)
        t1 = time.perf_counter()
        if i == 0:
            nvtx.RangePop()
        t_total += t1 - t0

    num_communities = int(parts_df["partition"].nunique())

    print("Louvain complete.")
    print("Detected communities:", num_communities)
    print("Modularity:", float(modularity_score))
    print(f"Avg Processing Time: {t_total / test_iter * 1000:.4f} ms.")


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python louvain_batch.py <graph_dir> <graph_k_list_file>")
        print("  python louvain_batch.py <graph_dir> <graph1> <k1> [<graph2> <k2> ...]")
        print("Example:")
        print("  python louvain_batch.py ./datasets graph_k_list.txt")
        print("  # where each row is: graph_name, k_value")
        print("  # k_value is validated but ignored for Louvain")
        print("  python louvain_batch.py ./datasets graph_a.tsv 4 graph_b 6")
        sys.exit(1)

    graph_dir = sys.argv[1]

    try:
        if len(sys.argv) == 3:
            graph_k_pairs = parse_graph_k_file(sys.argv[2])
        else:
            graph_k_pairs = parse_graph_k_pairs(sys.argv[2:])
    except (ValueError, FileNotFoundError) as exc:
        print(f"Argument error: {exc}")
        sys.exit(1)

    for idx, (graph_name, k_value) in enumerate(graph_k_pairs, start=1):
        print("\n" + "=" * 72)
        print(
            f"[{idx}/{len(graph_k_pairs)}] Graph='{graph_name}' "
            f"(ignoring k={k_value} for Louvain)"
        )

        try:
            graph_path, graph_format = resolve_graph_path(graph_dir, graph_name)
            print(f"Using file: {graph_path}")
            run_louvain_once(graph_path, graph_format)
        except Exception as exc:
            print(f"Failed for graph '{graph_name}': {exc}")


if __name__ == "__main__":
    main()
