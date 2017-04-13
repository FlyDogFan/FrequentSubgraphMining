
import networkx as nx

def create_nx_graph(origin_id, origin_label, target_id, target_label, edge_label):
    graph = nx.Graph()
    graph.add_node(origin_id, label=origin_label)
    graph.add_node(target_id, label=target_label)
    graph.add_edge(origin_id, target_id, label=edge_label)
    return nx.freeze(graph)

def extend_nx_graph(prev_graph, origin_node_id, target_node_id, node_label, edge_label):
    graph = nx.Graph(prev_graph)
    graph.add_node(target_node_id, label=node_label)
    graph.add_edge(origin_node_id, target_node_id, label=edge_label)
    return nx.freeze(graph)

def frontier_set(source_graph, current_graph, prev_frontier_edges, node_added, edge_to_remove):
    neighbors = source_graph.neighbors_iter(node_added)
    current_edges = current_graph.edge[node_added]

    new_frontier_edges = set(
        (node_added, neighbor_id) for neighbor_id in neighbors if neighbor_id not in current_edges
    )
    return prev_frontier_edges.union(new_frontier_edges) - set([edge_to_remove])