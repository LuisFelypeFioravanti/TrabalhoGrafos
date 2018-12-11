import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp


G=nx.Graph()


for i in range (0,100):
    G.add_node(i,pos=())
G.add_node(i,pos=(i,i))
G.add_node(2,pos=(2,2))
G.add_node(3,pos=(1,0))
G.add_edge(1,2,weight=0.5)
G.add_edge(1,3,weight=9.8)
pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos)
A = nx.adjacency_matrix(G)
print(A.todense())
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.draw()
plt.show()

