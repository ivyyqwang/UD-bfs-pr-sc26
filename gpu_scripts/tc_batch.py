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

def parse_graph_k_file(list_file_path):
    if not os.path.isfile(list_file_path):
        raise FileNotFoundError(f"Graph list file not found: {list_file_path}")

    graph_names = []
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
            if not graph_name:
                raise ValueError(
                    f"Invalid graph_name at line {line_num} in {list_file_path}"
                )

            try:
                int(parts[1])
            except ValueError as exc:
                raise ValueError(
                    f"Invalid k_value at line {line_num} in {list_file_path}: {parts[1]}"
                ) from exc

            graph_names.append(graph_name)

    if not graph_names:
        raise ValueError(f"No valid graph,k entries found in file: {list_file_path}")

    return graph_names


def run_triangle_count_once(graph_file, graph_format, warmup_iter=2, test_iter=5):
    if graph_format == "txt":
        G = load_txt_to_cugraph(graph_file)
    elif graph_format == "mtx":
        G = load_mtx_to_cugraph(graph_file)
    else:
        G = load_tsv_to_cugraph(graph_file)
    # G_copy = cugraph.Graph(directed=G.is_directed())

    # df = G.view_edge_list()
    # print(df["src"].dtype, df["dst"].dtype)
    # if "weight" in df.columns:
    #     G_copy.from_cudf_edgelist(df, source="src", destination="dst", edge_attr="weight")
    # else:
    #     G_copy.from_cudf_edgelist(df, source="src", destination="dst")

    print("Number of vertices:", G.number_of_vertices())
    print("Number of edges:", G.number_of_edges())

    for _ in range(warmup_iter):
        tc_result = cugraph.triangle_count(G)

    t_total = 0.0
    for i in range(test_iter):
        t_tc0 = time.perf_counter()
        if i == 0:
            nvtx.RangePush("tc")
        tc_result = cugraph.triangle_count(G)
        t_tc1 = time.perf_counter()
        if i == 0:
            nvtx.RangePop()
        t_total += t_tc1 - t_tc0

    total_triangle_count = int(tc_result["counts"].sum() // 3)
    print(f"Total Triangle Count: {total_triangle_count}")
    print("TC complete.")
    print(f"Avg Processing Time: {t_total / test_iter * 1000:.4f} ms.")


def main():
    if len(sys.argv) != 3:
        print("Usage:")
        print("  python tc_batch.py <graph_dir> <graph_k_list_file>")
        print("Example:")
        print("  python tc_batch.py ./datasets graph_k_list.txt")
        print("  # where each row is: graph_name, k_value")
        print("  # k_value is validated but ignored for triangle count")
        sys.exit(1)

    graph_dir = sys.argv[1]
    list_file = sys.argv[2]

    try:
        graph_names = parse_graph_k_file(list_file)
    except (ValueError, FileNotFoundError) as exc:
        print(f"Argument error: {exc}")
        sys.exit(1)

    for idx, graph_name in enumerate(graph_names, start=1):
        print("\n" + "=" * 72)
        print(f"[{idx}/{len(graph_names)}] Graph='{graph_name}'")

        try:
            graph_path, graph_format = resolve_graph_path(graph_dir, graph_name)
            print(f"Using file: {graph_path}")
            run_triangle_count_once(graph_path, graph_format)
        except Exception as exc:
            print(f"Failed for graph '{graph_name}': {exc}")


if __name__ == "__main__":
    main()
