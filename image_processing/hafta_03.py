#!/usr/bin/python3
# created by cicek on Oct 22, 2020 12:45 PM

import numpy as np
import matplotlib.pyplot as plt
import os


# resimleri al
def get_png_files():
    print(os.getcwd())  # /home/cicek/PycharmProjects/image_processing
    print(os.listdir())
    # ['.idea', 'README.md', 'hafta_01.py', 'figure_1.png',
    # 'hafta_02.py', 'venv', 'pic_1.jpg'] ['figure_1.png', 'pic_1.jpg']
    path = os.getcwd()
    jpg_files = [f for f in os.listdir(path) if f.endswith('.jpeg')]
    print(jpg_files)  # ['figure_1.png', 'pic_1.jpg']

    # im_1 = plt.imread(jpg_files[0])
    # print(im_1.shape)  # (480, 640, 4)
    # print(im_1.ndim)  # 3

    os.getcwd()
    os.listdir()
    return jpg_files


# ortalama RGB değeri ver
def get_value_from_triple(temp):
    return int(temp[0] / 3 + temp[1] / 3 + temp[2] / 3)


# bw için sadece 0 veya 1 yolla
def get_0_1_from_triple(temp_1):
    temp = int(temp_1[0] / 3 + temp_1[1] / 3 + temp_1[2] / 3)
    if temp < 110:
        return 0
    else:
        return 1


# grey level 'a çevir
def convert_rgb_to_gray(image):
    m, n, k = image.shape
    new_image = np.zeros((m, n), dtype='uint8')
    for i in range(m):
        for j in range(n):
            s = get_value_from_triple(image[i, j, :])
            new_image[i, j] = s
    return new_image


# rgb -> siyah beyaza çevir
def convert_rgb_to_bw(image):
    m, n, k = image.shape
    new_image = np.zeros((m, n), dtype='uint8')
    for i in range(m):
        for j in range(n):
            s = get_0_1_from_triple(image[i, j, :])
            new_image[i, j] = s
    return new_image


# ana resmi al
jpg = get_png_files()
im_1 = plt.imread(jpg[0])  # intensity, energy level

# (0x, 0y) deki ortalama RGB değer
value = get_value_from_triple(im_1[0, 0, :])
print(value)  # 138

# grey level resmi al
im_2 = convert_rgb_to_gray(im_1)

# siyah beyaz resmi al
im_3 = convert_rgb_to_bw(im_1)

# 3 jpeg resmi ekrana ver
plt.subplot(1, 3, 1)
plt.imshow(im_1)
plt.subplot(1, 3, 2)
plt.imshow(im_2, cmap='gray')
plt.subplot(1, 3, 3)
plt.imshow(im_3, cmap='gray')
plt.show()

# plt.imsave('home_gray.jpeg', im_2, cmap='gray')

# # im_1[10,30] = 45
# print(im_1.shape)  # (851, 1280, 3)
# print(im_1.ndim)  # 3
# print(im_1[0, 0, 0])  # (row, col, rgb) 150
