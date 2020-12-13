#!/usr/bin/python3
# created by cicek on Nov 20, 2020 6:05 PM

# dilation - genişletme(sulandırma)
'''
resmin içindeki objeyi kenarlarına doğru genişletiyor.
arka plan 0 ise resmin kenarlarındaki 0 ları 1 yapar

'''

import matplotlib.pyplot as plt
import math
import numpy as np


def convert_rgb_to_monochrome_bw(image_1, threshold=100.0):
    img_1 = image_1
    img_2 = np.zeros((img_1.shape[0], img_1.shape[1]))

    for i in range(img_2.shape[0]):
        for j in range(img_2.shape[1]):
            if (img_1[i, j, 0] / 3 + img_1[i, j, 1] / 3 + img_1[i, j, 1] / 3) > threshold:
                img_2[i, j] = 0
            else:
                img_2[i, j] = 1
    return img_2


def m_f_0_and(l1, l2):
    n = len(l1)
    s = []
    for i in range(n):
        a = l1[i] and l2[i]
        s.append(a)
    return s


def m_f_1_and_or_or(l1, operator=0):
    if operator:
        if 1 in l1:
            s1 = 1
        else:
            s1 = 0
    else:
        if 0 in l1:
            s1 = 0
        else:
            s1 = 1

    return s1


def m_f_2_combine(l1, l2, op=0):
    a = m_f_0_and(l1, l2)
    return m_f_1_and_or_or(a, op)


def define_mask_1():
    mask_1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    return mask_1


def define_mask_2():
    mask_1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return mask_1


def my_dilation(img__1, mask):
    m = img__1.shape[0]  # 100
    n = img__1.shape[1]  # 100
    img__2 = np.zeros((m, n), dtype='uint8')

    for i in range(1, m - 1):  # padding
        for j in range(1, n - 1):
            # apply mask_1 for dilation
            x_1 = img__1[i, j] == mask[1][1]

            x_2 = img__1[i - 1, j - 1] == mask[0][0]
            x_3 = img__1[i - 1, j] == mask[0][1]
            x_4 = img__1[i - 1, j + 1] == mask[0][2]

            x_5 = img__1[i + 1, j - 1] == mask[2][0]
            x_6 = img__1[i + 1, j] == mask[2][1]
            x_7 = img__1[i + 1, j + 1] == mask[2][2]

            x_8 = img__1[i, j - 1] == mask[1][0]
            x_9 = img__1[i, j + 1] == mask[1][2]

            result_1 = x_1 or x_2 or x_3 or x_4 or x_5
            result_2 = x_6 or x_7 or x_8 or x_9

            result = result_1 or result_2

            img__2[i, j] = result

    return img__2


# list_1 = [0, 0, 1, 0, 1]  # mask
# list_2 = [1, 1, 1, 1, 1]  # block
# # image_or = (list_1[0] and list_2[0]) or (list_1[1] and list_2[1]) or (list_1[2] and list_2[2])
# # print(image_or)  # 1
#
# # a = m_f_0_and(list_1, list_2)
# # print(m_f_1_and_or_or(a))
#
# a = m_f_2_combine(list_1, list_2, 1)
# print(a)  # 1

path_file = r"/home/cicek/PycharmProjects/image_processing/pixel.png"
img_1 = plt.imread(path_file)

img_2 = convert_rgb_to_monochrome_bw(img_1, 0.5)

img_3 = my_dilation(img_2, define_mask_1())

plt.subplot(1, 3, 1), plt.imshow(img_1)
plt.subplot(1, 3, 2), plt.imshow(img_2, cmap='gray')
plt.subplot(1, 3, 3), plt.imshow(img_3, cmap='gray')
plt.show()  # dilation_3d.png
