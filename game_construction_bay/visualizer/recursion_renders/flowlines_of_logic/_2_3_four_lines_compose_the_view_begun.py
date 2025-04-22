# Filename: _2_3_four_lines_compose_the_view_begun.py

import networkx as nx


def compose_stanza_view(graph: nx.DiGraph, stanza_id: str, line_ids: list[str]) -> nx.DiGraph:
    """
    Renders the emerging stanza structure as a cohesive visual quartet—highlighting symmetry, balance,
    and recursive buildup between the four lines.

    Args:
        graph (nx.DiGraph): The active recursion graph containing prior verse and flowline nodes.
        stanza_id (str): A unique ID representing the full stanza (e.g., "stanza_2").
        line_ids (list[str]): A list of exactly four node IDs corresponding to the lines in the stanza.

    Returns:
        nx.DiGraph: The graph with stanza grouping logic added.
    """
    assert len(line_ids) == 4, "A stanza must consist of exactly four lines."

    stanza_node = f"{stanza_id}_view"
    graph.add_node(stanza_node, label=f"Stanza: {stanza_id}", type="stanza_view", style="quartet")

    for line_id in line_ids:
        if line_id not in graph:
            graph.add_node(line_id, label=f"Line: {line_id}", type="unclassified_line")
        graph.add_edge(stanza_node, line_id, type="stanza_composition")

    return graph
