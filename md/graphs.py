import networkx as nx
import pickle
cm = pickle.load(open('/mnt/supermicro/avocado/1458/correlations_c.pkl','rb'))
cm
G = nx.Graph(cm)
G
G.nodes
G.edges
import matplotlib as plt
import io
import base64
nx.draw_networkx(G,pos=nx.spring_layout(G,k=0.1), node_color=bc, node_size=5, font_size=0.5, width=0.05, edge_color=wghts, edge_cmap=plt.cm.RdBu, edge_vmax=1, edge_vmin=-1,
     ...:  alpha=0.5)
weights = []
for k in cm.keys():
    for kk in cm[k].keys():
        weights.append((k,kk,cm[k][kk]))
weights
G.add_weighted_edges_from(weights)
nx.is_weighted(G)
nx.is_weighted(G)
 bc = list(nx.betweenness_centrality(G,weight="weight").values())
bc
bc
wghts = [G[k][v]['weight'] for k,v in G.edges]
nx.draw_networkx(G,pos=nx.spring_layout(G,k=0.1), node_color=bc, node_size=5, font_size=0.5, width=0.05, edge_color=wghts, edge_cmap=plt.cm.RdBu, edge_vmax=1, edge_vmin=-1, alpha=0.5)
img = io.BytesIO()
import matplotlib.pyplot as plt
plt.savefig(img,dpi=300)
plot_url = base64.b64encode(img.getvalue()).decode()
plot_url
/len plot_url
%history -f graphs.py
