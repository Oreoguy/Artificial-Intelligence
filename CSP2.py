import networkx as nx
import matplotlib.pyplot as plt

# Read inputs
#1
N_V = int(input("Enter total number of variables: "))

#2
variables = input("Enter variable names (separated by spaces): ").split()

#3
domains = {}
for var in variables:
    domains[var] = list(map(int, input(f"Enter domain of {var} (separated by spaces): ").split()))

#4
N_UC = int(input("Enter total number of unary constraints: "))

#5
unary_constraints = []
for i in range(N_UC):
    constraint = input(f"Enter unary constraint {i+1}: ")
    var, operator, constant = constraint.split()
    unary_constraints.append((var, operator, int(constant)))

#6    
N_BC = int(input("Enter total number of binary constraints: "))
binary_constraints = []
for i in range(N_BC):
    constraint = input(f"Enter binary constraint {i+1}: ")
    var1, operator, var2, op, constant = constraint.split()
    binary_constraints.append((var1, operator, var2, op, int(constant)))

# Adjust variable domains based on unary constraints
for var, values in domains.items():
    for constraint in unary_constraints:
        if constraint[0] == var:
            operator, constant = constraint[1:]
            if operator == "<":
                values = [v for v in values if v < constant]
            elif operator == ">":
                values = [v for v in values if v > constant]
            elif operator == "<=":
                values = [v for v in values if v <= constant]
            elif operator == ">=":
                values = [v for v in values if v >= constant]
            elif operator == "==":
                values = [v for v in values if v == constant]
            elif operator == "!=":
                values = [v for v in values if v != constant]
    domains[var] = values

# Create graph and add nodes
graph = nx.Graph()
graph.add_nodes_from(variables)

# Add edges based on binary constraints
for constraint in binary_constraints:
    var1, operator, var2, op, constant = constraint
    if operator == "<":
        graph.add_edge(var1, var2, weight=constant)
    elif operator == ">":
        graph.add_edge(var2, var1, weight=constant)
    elif operator == "<=":
        graph.add_edge(var1, var2, weight=constant+1)
    elif operator == ">=":
        graph.add_edge(var2, var1, weight=constant+1)
    elif operator == "==":
        pass
    elif operator == "!=":
        for value1 in domains[var1]:
            for value2 in domains[var2]:
                if value1 != value2:
                    graph.add_edge(var1, var2)

# Draw graph
pos = nx.circular_layout(graph)
nx.draw(graph, pos, with_labels=True, font_weight='bold')
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_weight='bold')
plt.show()
