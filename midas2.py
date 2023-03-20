import networkx as nx
import matplotlib.pyplot as plt

# Define the relations between entities as a list of tuples
relations = [
    ('King Midas', 'Gold', 'possesses'),
    ('King Midas', 'Daughter', 'had and loves'),
    ('King Midas', 'Angel', 'Meets'),
    ('Angel', 'Needs Help', 'from Midas'),
    ('Angel', 'Wish', 'grants'),
    ('Wish', 'Gold Touch', 'turns everything to gold'),
    ('Gold Touch', 'Daughter', 'Hugs in excitement'),
    ('Daughter','Gold','turns to'),
    ('Gold','Devastated','is'),
    ('Devastated','Angel','Take the wish away')
]

# Create a directed graph using NetworkX
G = nx.DiGraph()
for start, end, relation in relations:
    G.add_edge(start, end, label=relation)

# Define the positions of the nodes using the spring layout algorithm
pos = nx.shell_layout(G)

# Draw the graph nodes and edges with labels using Matplotlib
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='lightblue')
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='black')
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

for i in range (len(relations)):
    x, y, z = relations[i]
    print(x,z,y)

# Show the plot
plt.axis('off')
plt.show()
