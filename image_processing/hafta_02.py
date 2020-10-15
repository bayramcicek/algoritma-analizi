#!/usr/bin/python3
# created by cicek on Oct 15, 2020 2:47 PM

import numpy as np
import matplotlib.pyplot as plt
import os


def get_png_files():
    print(os.getcwd())  # /home/cicek/PycharmProjects/image_processing
    print(os.listdir())
    # ['.idea', 'README.md', 'hafta_01.py', 'figure_1.png',
    # 'hafta_02.py', 'venv', 'pic_1.jpg'] ['figure_1.png', 'pic_1.jpg']
    path = os.getcwd()
    jpg_files = [f for f in os.listdir(path) if f.endswith('.png')]
    print(jpg_files)  # ['figure_1.png', 'pic_1.jpg']

    # im_1 = plt.imread(jpg_files[0])
    # print(im_1.shape)  # (480, 640, 4)
    # print(im_1.ndim)  # 3

    os.getcwd()
    os.listdir()
    return jpg_files


def compare_list_ndarray():
    list_1 = [1, 2, 'test', 4, '5']  # farklı veriler
    list_2 = [1, 2, 3, 4]  # aynı tip veriler
    print(list_2 + list_2 + [10])  # [1, 2, 3, 4, 1, 2, 3, 4, 10]
    # (list_2 + list_2 + 10) -> error

    # broadcasting desteği için np, ndarray asarray
    list_3 = np.asarray([1, 2, 3, 4])
    list_4 = np.asarray([1, 2, 3, 4])
    print(list_3 + list_4)  # [2 4 6 8]
    print(list_3 + list_4 + 10)  # [12 14 16 18]


def display_two_image(im_1, im_2):
    plt.subplot(1, 2, 1)
    plt.imshow(im_1)

    plt.subplot(1, 2, 2)
    plt.imshow(im_2)
    plt.show()


def rotate(im_1):
    m, n, k = im_1.shape
    new_image = np.zeros((n, m, k), dtype='uint8')
    for i in range(m):
        for j in range(n):
            temp = im_1[i, j]
            new_image[j, i] = temp
    return new_image


get_png_files()
compare_list_ndarray()

image_1 = plt.imread('pic_1.jpg')
print(type(image_1))  # <class 'numpy.ndarray'>
print(image_1.ndim)  # 3

image_2 = image_1 + 10
print(image_1.shape, image_2.shape)
# (480, 360, 3) (480, 360, 3)

print(image_1[25, 300, :], image_2[25, 300, :])
# [122 146 232] [132 156 242]

# image_2 göster
image_2 = rotate(image_1)
display_two_image(image_1, image_2)  # figure_2_90.png

# image_3 göster
image_3 = rotate(image_2)
display_two_image(image_1, image_3)  # figure_3_normal.png
