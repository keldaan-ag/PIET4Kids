import numpy as np

#TODO Make a hysteresis threshold  https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.apply_hysteresis_threshold

def threshold(img, threshold):
    img_threshold = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] > threshold:
                img_threshold[i, j] = 255
            else:
                img_threshold[i, j] = 0
    return img_threshold
