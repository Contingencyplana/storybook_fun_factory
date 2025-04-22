# Filename: _2_2_each_path_a_map_from_what_was_said.py

import networkx as nx


def map_logical_flow_from_expression(
    graph: nx.DiGraph,
    origin_id: str,
    derived_ids: list[str],
    metadata: dict = None
) -> nx.DiGraph:
    """
    Constructs the logical flowlines that emerge from spoken or inscribed recursion.
    It maps past expressions into branching visual pathways.

    Args:
        graph (nx.DiGraph): The visual recursion graph.
        origin_id (str): Node ID where the expression originated (e.g., a verse or decision).
        derived_ids (list[str]): List of node IDs that represent the logical paths derived from the origin.
        metadata (dict, optional): Additional metadata applied to the origin node.

    Returns:
        nx.DiGraph: The updated graph with new expression flow paths.
    """
    if metadata is None:
        metadata = {}

    # Add origin node if not already present
    if origin_id not in graph:
        graph.add_node(origin_id, label=f"Expr: {origin_id}", type="expression_origin", **metadata)

    # Add derived nodes and edges
    for target_id in derived_ids:
        if target_id not in graph:
            graph.add_node(target_id, label=f"Path: {target_id}", type="expression_branch")
        graph.add_edge(origin_id, target_id, type="expression_flow")

    return graph
