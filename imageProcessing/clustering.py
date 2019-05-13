import numpy as np
from .graphObjects import graphObjects

# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
# https://www.programiz.com/python-programming/methods/built-in/sorted

# D(n ∪ m) ≤ min(D(n), D(m)) + KD/|n ∪ m|
# M(n ∪ m) ≤ min(M(n), M(m)) + KM/|n ∪ m|


def get_weighted_graph(img_threshold, magnitudes, directions):
    graph = GraphWeightArrayEnv(img_threshold, magnitudes, directions)
    return graph.compute_weighted_graph()


def get_picture_weighted_graph(img, weighted_graph):
    picture = np.zeros(img.shape)
    for i in range(len(weighted_graph)):
        random_color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
        for node in weighted_graph[i]:
            picture[node.x, node.y] = random_color
    return picture


class GraphWeightArrayEnv:

    def __init__(self, img_threshold, magnitudes, directions):
        self.img_threshold = img_threshold
        self.magnitudes = magnitudes
        self.directions = directions
        self.graph = []
        self.current_connected_component = set()
        #1) Initialize all vertices as not visited.
        self.visited_array = np.ones(img_threshold.shape, dtype=bool)

    def compute_weighted_graph(self):
        #2) Do following for every vertex 'v'.
        for i in range(self.img_threshold.shape[0]):
            for j in range(self.img_threshold.shape[1]):
                if self.img_threshold[i, j]:
                    #(a) If 'v' is not visited before, call DFSUtil(v)
                    if self.visited_array[i, j]:
                        self.depth_first_search(i, j)
                        self.graph.append(self.current_connected_component)
                        self.current_connected_component = set()

        return self.graph

    def depth_first_search(self, i, j):
        self.visited_array[i, j] = False
        self.current_connected_component.add(graphObjects.Node(i, j, self.magnitudes[i, j], self.directions[i, j]))

        #left check
        if i - 1 >= 0:
            if self.visited_array[i - 1, j] and self.img_threshold[i - 1, j]:
                self.depth_first_search(i - 1, j)
        #right check
        if i + 1 < self.img_threshold.shape[0]:
            if self.visited_array[i + 1, j] and self.img_threshold[i + 1, j]:
                self.depth_first_search(i + 1, j)
        #top check
        if j - 1 >= 0:
            if self.visited_array[i, j - 1] and self.img_threshold[i, j - 1]:
                self.depth_first_search(i, j - 1)
        #bottom check
        if j + 1 < self.img_threshold.shape[1]:
            if self.visited_array[i, j + 1] and self.img_threshold[i, j + 1]:
                self.depth_first_search(i, j + 1)







