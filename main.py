import imageio
import os
from imageProcessing.sobel import sobel_filter
from imageProcessing.threshold import threshold
from imageProcessing.clustering import get_weighted_graph, get_picture_weighted_graph

base_dir = r"C:\Users\arnau\OneDrive\Bureau\PIET4Kids"
img_dir = os.path.join(base_dir, "img")

print("loading picture as array...")
img = imageio.imread(os.path.join(img_dir, "test.jpg"))

print("computing edge gradient intensity and edge grandient direction...")
(edge_gradient, edge_angle) = sobel_filter(img)

print("Computing threshold...")
img_threshold = threshold(edge_gradient, 1)

print("Creating weighted graph...")
weighted_graph = get_weighted_graph(img_threshold, edge_gradient, edge_angle)
img_graph = get_picture_weighted_graph(img, weighted_graph)
print(weighted_graph)

imageio.imsave(os.path.join(img_dir, "edge_angle.jpg"), edge_angle)
imageio.imsave(os.path.join(img_dir, "edge_gradient.jpg"), edge_gradient)
imageio.imsave(os.path.join(img_dir, "img_graph.jpg"), img_graph)
