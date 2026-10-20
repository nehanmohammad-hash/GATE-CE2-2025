import os
import matplotlib.pyplot as plt
import networkx as nx

# Ensure the target directory exists
os.makedirs("../../figs", exist_ok=True)

# 1. Initialize a Directed Graph
G = nx.DiGraph()

# 2. Add edges with labels representing activities and durations
edges = [
    (1, 2, {"label": "A\n3 days"}),
    (1, 3, {"label": "C\n5 days"}),
    (2, 4, {"label": "B\n5 days"}),
    (3, 4, {"label": "D\n2 days"}),
    (3, 5, {"label": "F\n8 days"}),
    (4, 5, {"label": "E\n4 days"}),
]

G.add_edges_from(edges)

# 3. Define custom node coordinates to match the visual layout of the image
pos = {
    1: (0, 1),  # Starting node
    2: (1, 2),  # Top branch
    3: (1, 0),  # Bottom branch
    4: (2, 1),  # Convergence node
    5: (3, 1),  # Ending node
}

# 4. Set up the plot layout
plt.figure(figsize=(9, 5))

# Draw the nodes (white circles with black borders)
nx.draw_networkx_nodes(
    G, pos, node_size=700, node_color="white", edgecolors="black", linewidths=1.5
)

# Draw the node labels (numbers inside the circles)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

# Draw the directed edges with arrows
nx.draw_networkx_edges(
    G,
    pos,
    edge_color="black",
    width=1.5,
    arrowstyle="-|>",
    arrowsize=15,
    connectionstyle="arc3,rad=0",
)

# Draw the edge labels (activity letters and durations)
edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.5
)

# Display the plot styling
plt.title("Project Network Diagram (PERT/CPM)", fontsize=14, fontweight="bold")
plt.axis("off")
plt.tight_layout()

# 5. Save the figure to the specified path
plt.savefig("../../figs/network_diagram.png", dpi=300, bbox_inches="tight")
plt.close()

print("Figure successfully saved to ../../figs/network_diagram.png")
