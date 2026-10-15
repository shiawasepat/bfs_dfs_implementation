import networkx as nx
import matplotlib.pyplot as plt

from routes import graph
from bfs import bfs
from dfs import dfs

start_node = 'Rumah'
goal_node = 'Kampus UC'

print("=== Pencarian Jalur dari {} ke {} ===\n".format(start_node, goal_node))

jalur_bfs = bfs(graph, start_node, goal_node)
print("Jalur menggunakan BFS:")
print(" -> ".join(jalur_bfs) if jalur_bfs else "Jalur tidak ditemukan")

print("\nJalur menggunakan DFS:")
jalur_dfs = dfs(graph, start_node, goal_node)
print(" -> ".join(jalur_dfs) if jalur_dfs else "Jalur tidak ditemukan")

# Membangun graf dari dictionary
G = nx.DiGraph(graph)

# Fungsi untuk memvisualisasikan jalur
def draw_path(G, path, title):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=10)
    
    # Menggambar seluruh graf
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=3000, 
            edge_color='lightgray', width=2, font_size=10, font_weight='bold', arrowsize=20)
    
    # Menyoroti jalur yang ditemukan
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='yellow', node_size=3000)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3, arrowsize=25)
        
    plt.title(title, fontsize=14)
    plt.show()

# Menampilkan visualisasi
if jalur_bfs:
    draw_path(G, jalur_bfs, "Visualisasi Jalur BFS")

if jalur_dfs:
    draw_path(G, jalur_dfs, "Visualisasi Jalur DFS")

# Menambahkan layer ke setiap node
layers = list(nx.topological_generations(G))

for layer_number, nodes in enumerate(layers):
    for node in nodes:
        G.nodes[node]["layer"] = layer_number

pos = nx.multipartite_layout(
    G,
    subset_key="layer",
    align="vertical",
    scale=2
)
