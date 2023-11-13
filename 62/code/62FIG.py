import matplotlib.pyplot as plt
import networkx as nx

# Define birth and death rates
lambda_values = [1, 1, 2, 0]
mu_values = [0, 1, 1, 1]

# Create directed graph
G = nx.DiGraph()

# Add nodes with labels
states = [0, 1, 2, 3]
G.add_nodes_from(states)
labels = {0: '0', 1: '1', 2: '2', 3: '3'}

# Add edges with rates as labels
for i in range(len(states) - 1):
    G.add_edge(states[i], states[i+1], label=f'λ{states[i]}→{states[i+1]}')
    G.add_edge(states[i+1], states[i], label=f'µ{states[i+1]}→{states[i]}')

# Set layout for the graph
pos = {0: (0, 0), 1: (1, 0), 2: (2, 0), 3: (3, 0)}

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')

# Draw edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# Draw labels
nx.draw_networkx_labels(G, pos, labels=labels, font_size=12)

# Draw curved arrows for births and deaths
for i in range(len(states) - 1):
    # Curved arrow for births
    plt.annotate(
        '', xy=pos[states[i+1]], xytext=pos[states[i]],
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.3", color='green')
    )
    
    # Label for λ values
    plt.text(
        pos[states[i+1]][0] - 0.1, pos[states[i+1]][1] - 0.1, f'λ{states[i]}={lambda_values[i]}',
        horizontalalignment='center', verticalalignment='center', color='green'
    )

    # Curved arrow for deaths
    plt.annotate(
        '', xy=pos[states[i+1]], xytext=pos[states[i]],
        arrowprops=dict(arrowstyle="<-", connectionstyle="arc3,rad=0.3", color='red')
    )
    
    # Label for µ values
    plt.text(
        pos[states[i+1]][0], pos[states[i+1]][1] + 0.1, f'µ{states[i+1]}={mu_values[i+1]}',
        horizontalalignment='center', verticalalignment='center', color='red'
    )



# Show the plot
plt.title('Markov Chain for Birth-Death Process')
plt.axis('off')  # Turn off axis
plt.show()

