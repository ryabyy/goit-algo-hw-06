import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([("D", "S"), ("I", "D"), ("I", "V"), ("V", "D"), ("I", "U1"), ("I", "U2"), ("I", "U3")])

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
is_connected = nx.is_connected(G)

print(f"The graph has {num_nodes} nodes, linked by {num_edges} edges. The graph is{' not' if not is_connected else ''} connected.")

print("\nNode degrees:")
for node in G.nodes:
	print(f"Node {node} has degree {G.degree(node)}")

source = "U1"
dfs_tree = nx.dfs_tree(G, source=source)
print(f"\nDFS search starting at {source}")
print(list(dfs_tree.edges()))

bfs_tree = nx.bfs_tree(G, source=source)
print(f"\nBFS search starting at {source}")
print(list(bfs_tree.edges()))

G.add_weighted_edges_from([("D", "S", 1), ("I", "D", 1), ("I", "V", 1), ("V", "D", 1), ("I", "U1", 5), ("I", "U2", 5), ("I", "U3", 5)])

for source in G.nodes:
	shortest_paths = nx.single_source_dijkstra_path(G, source=source, cutoff=None)
	shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source=source, cutoff=None)
	print(f"\nShortest paths from {source} to other nodes:")
	for node in G.nodes:
		print(f"Shortest path from {source} to {node} has distance of {shortest_path_lengths[node]}. Route: {shortest_paths[node]}")

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=800, node_color="skyblue")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()