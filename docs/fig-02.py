import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes
input_nodes = ["Input1", "Input2", "Input3"]
junction_nodes = ["J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10"]
output_nodes = ["Output1", "Output2", "Output3", "Output4"]

# Add nodes to the graph
G.add_nodes_from(input_nodes + junction_nodes + output_nodes)

# Define edges (connections between nodes)
edges = [
    ("Input1", "J1"), ("Input1", "J2"), ("Input1", "J3"),
    ("Input2", "J3"), ("Input2", "J4"), ("Input2", "J5"),
    ("Input3", "J5"), ("Input3", "J6"), ("Input3", "J7"),
    ("J1", "J8"), ("J2", "J8"), ("J3", "J8"), ("J4", "J9"), ("J5", "J9"), ("J6", "J9"),
    ("J7", "J10"), ("J8", "Output1"), ("J9", "Output2"), ("J10", "Output3")
]

# Add edges to the graph
G.add_edges_from(edges)

# Define positions for nodes (similar to a neural network layout)
pos = {
    "Input1": (0, 2), "Input2": (0, 0), "Input3": (0, -2),
    "J1": (1, 3), "J2": (1, 2), "J3": (1, 1), "J4": (1, 0), "J5": (1, -1), "J6": (1, -2), "J7": (1, -3),
    "J8": (2, 2), "J9": (2, 0), "J10": (2, -2),
    "Output1": (3, 2), "Output2": (3, 0), "Output3": (3, -2), "Output4": (3, -3)
}

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue", alpha=0.7)

# Draw the edges
nx.draw_networkx_edges(G, pos, width=2, arrowstyle='-|>', arrowsize=15, edge_color='gray')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")

# Add title
plt.title("Pipe Maze Environment with Unconnected Output4")

# Show the plot
plt.show()
