#!/usr/bin/python3
# created by cicek on Nov 24, 2020 2:45 PM

import matplotlib.pyplot as plt
import numpy as np


def get_mask_for_edge():
    return np.array([-1, 0, 1, -2, 0, 2, -1, 0, 1]).reshape(3, 3)


def apply_mask_for_edge(part_of_image):
    mask = get_mask_for_edge()
    return sum(sum(part_of_image * mask))


def get_edges(image):
    m = image.shape[0]
    n = image.shape[1]

    image2 = np.zeros((m, n))

    for i in range(3, m - 3):
        for j in range(3, n - 3):
            poi = image[i - 1:i + 2, j - 1:j + 2]
            image2[i, j] = apply_mask_for_edge(poi)

    return image2


def convert_rgb_to_gray_level(img_1):
    m = img_1.shape[0]
    n = img_1.shape[1]
    im__2 = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            im__2[i, j] = get_distance(img_1[i, j, :])
    return im__2


def get_distance(v, w=None):
    if w is None:
        w = [1 / 3, 1 / 3, 1 / 3]
    a, b, c = v[0], v[1], v[2]
    w1, w2, w3 = w[0], w[1], w[2]
    d = ((a ** 2) * w1 +
         (b ** 2) * w2 +
         (c ** 2) * w3) ** .5
    return d


# print(apply_mask_for_edge(get_mask_for_edge()))  # 12

im_1 = plt.imread('pic_1.jpg')
im_2 = convert_rgb_to_gray_level(im_1)
im_with_edges = get_edges(im_2)

plt.subplot(1, 3, 1), plt.imshow(im_1)
plt.subplot(1, 3, 2), plt.imshow(im_2, cmap='gray')
plt.subplot(1, 3, 3), plt.imshow(im_with_edges, cmap='gray')  # edge_troia.png
plt.show()
