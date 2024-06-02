import networkx as nx
import matplotlib.pyplot as plt


graph = {
    'Biratnagar': {
        'Ithari':22,
        'Biratchowk':30,
        'Rangeli':25
    },
    'Ithari':{
        'Biratnagar':22,
        'Biratchowk':11,
        'Dharan':20
    },
    'Biratchowk':{
        'Biratnagar':30,
        'Ithari':11,
        'Kanepokhari':10
    },
    'Rangeli':{
        'Biratnagar':25,
        'Kanepokhari':25,
        'Urlabari':40
    },
    'Dharan':{
        'Ithari':20
    },
    'Kanepokhari':{
        'Biratchowk':10,
        'Rangeli':25,
        'Urlabari':12
    },
    'Urlabari':{
        'Kanepokhari':12,
        'Rangeli':40,
        'Damak':6
    },
    'Damak':{
        'Urlabari':6
    }
}


G = nx.Graph()

for node, neighbors in graph.items():
    for neighbor, distance in neighbors.items():
        G.add_edge(node, neighbor, weight=distance)

pos = nx.spring_layout(G)  
edges = G.edges(data=True)

# Draw nodes and edges
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['weight']} km" for u, v, d in edges}, font_color='red')

# Show plot
plt.title("Graph Representation of Cities and Distances")
plt.show()
