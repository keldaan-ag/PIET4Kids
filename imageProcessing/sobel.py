import numpy as np
import scipy.ndimage.filters as filters


def sobel_filter(img):
    sobel_filter_x = np.array(
        [[-1, 0, 1],
         [-2, 0, 2],
         [-1, 0, 1]])

    sobel_filter_y = np.array(
        [[-1, -2, -1],
         [0, 0, 0],
         [1, 2, 1]])

    img_gray = np.zeros((img.shape[0], img.shape[1]))

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # https://stackoverflow.com/questions/17615963/standard-rgb-to-grayscale-conversion
            img_gray[i, j] = 0.30 * img[i, j, 0] + 0.59 * img[i, j, 1] + 0.11 * img[i, j, 2]

    horizontal_gradient = filters.convolve(img_gray, sobel_filter_x)
    vertical_gradient = filters.convolve(img_gray, sobel_filter_y)

    edge_gradient = np.hypot(horizontal_gradient, vertical_gradient)
    edge_gradient = edge_gradient / np.std(edge_gradient)

    edge_angle = np.arctan2(vertical_gradient, horizontal_gradient)

    # imageio.imsave(os.path.join(img_dir, "horizontal_gradient.jpg"), horizontal_gradient)
    # imageio.imsave(os.path.join(img_dir, "vertical_gradient.jpg"), vertical_gradient)

    return edge_gradient, edge_angle
