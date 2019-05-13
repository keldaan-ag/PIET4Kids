import numpy as np

# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
# https://www.programiz.com/python-programming/methods/built-in/sorted

# D(n ∪ m) ≤ min(D(n), D(m)) + KD/|n ∪ m|
# M(n ∪ m) ≤ min(M(n), M(m)) + KM/|n ∪ m|

def compute_weighted_graph(img_threshold):
    nodes = getNodes(img_threshold)
    print(nodes)
    return nodes

def getNodes(img_threshold):
    nodes = []
    for i in range(img_threshold.shape[0]):
        for j in range(img_threshold.shape[1]):
            if img_threshold[i,j]:
                nodes.append((i,j))
    return nodes
