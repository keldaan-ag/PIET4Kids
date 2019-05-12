import numpy as np

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