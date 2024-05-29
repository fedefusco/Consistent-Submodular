from igraph import *
import pickle
import numpy as np

data = np.loadtxt('facebook_combined.txt', delimiter=',', skiprows=0, dtype=str)

vertices = set()      
edges = []

for edge in data:
    i,j = edge.split()
    vertices.add(int(i))
    vertices.add(int(j))
    edges.append((int(i), int(j)))

n = len(vertices)
g = Graph(n)  

g.add_edges(edges)

print(summary(g))

pickle.dump(g, open( "facebook_graph.p", "wb" ) )













