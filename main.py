import imageio
import os
from imageProcessing import sobel
from imageProcessing.threshold import threshold
import matplotlib.pyplot as plt
import numpy as np


base_dir = r"C:\Users\arnau\OneDrive\Bureau\PIET4Kids"
img_dir = os.path.join(base_dir, "img")

img = imageio.imread(os.path.join(img_dir, "test.jpg"))

edge_gradient = sobel.sobel_filter(img)
plt.hist(edge_gradient.flatten(), 100)
plt.show()

img_threshold = threshold(edge_gradient, 2)
imageio.imsave(os.path.join(img_dir, "img_threshold.jpg"), img_threshold)
imageio.imsave(os.path.join(img_dir, "edge_gradient.jpg"), edge_gradient)