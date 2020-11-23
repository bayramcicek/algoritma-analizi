#!/usr/bin/python3
# created by cicek on Nov 23, 2020 6:20 PM

# dilation - erosion - openin and closing

import matplotlib.pyplot as plt
import numpy as np


def convert_rgb_to_monochrome_bw(image_1, threshold=100.0):
    imgg_1 = image_1
    imgg_2 = np.zeros((imgg_1.shape[0], imgg_1.shape[1]))

    for i in range(imgg_2.shape[0]):
        for j in range(imgg_2.shape[1]):
            if (imgg_1[i, j, 0] / 3 + imgg_1[i, j, 1] / 3 + imgg_1[i, j, 1] / 3) > threshold:
                imgg_2[i, j] = 0
            else:
                imgg_2[i, j] = 1
    return imgg_2


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


def my_dilation(img__1, mask, morphology_operation='dilation'):
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

            if morphology_operation == 'dilation':
                result_1 = x_1 or x_2 or x_3 or x_4 or x_5
                result_2 = x_6 or x_7 or x_8 or x_9

                result = result_1 or result_2

            elif morphology_operation == 'erosion':
                result_1 = x_1 and x_2 and x_3 and x_4 and x_5
                result_2 = x_6 and x_7 and x_8 and x_9

                result = result_1 and result_2

            img__2[i, j] = result

    return img__2


path_file = r"/home/cicek/PycharmProjects/image_processing/pixel.png"

img_1 = plt.imread(path_file)
img_2 = convert_rgb_to_monochrome_bw(img_1, 0.5)

# img_3 = my_dilation(img_2, define_mask_1())
# img_4 = my_dilation(img_3, define_mask_1())
# img_5 = my_dilation(img_4, define_mask_1())

# # opening process
# img_3 = my_dilation(img_2, define_mask_1(), 'erosion')  # sihaylar artar
# img_4 = my_dilation(img_3, define_mask_1(), 'erosion')
# img_5 = my_dilation(img_4, define_mask_1(), 'erosion')
#
# img_6 = my_dilation(img_5, define_mask_1(), 'dilation')  # beyazlat
# img_7 = my_dilation(img_6, define_mask_1(), 'dilation')
# img_8 = my_dilation(img_7, define_mask_1(), 'dilation')

# closing process
img_3 = my_dilation(img_2, define_mask_1(), 'dilation')  # beyazlat
img_4 = my_dilation(img_3, define_mask_1(), 'dilation')
img_5 = my_dilation(img_4, define_mask_1(), 'dilation')

img_6 = my_dilation(img_5, define_mask_1(), 'erosion')  # siyahlat
img_7 = my_dilation(img_6, define_mask_1(), 'erosion')
img_8 = my_dilation(img_7, define_mask_1(), 'erosion')

plt.subplot(1, 4, 1), plt.imshow(img_1)
plt.subplot(1, 4, 2), plt.imshow(img_2, cmap='gray')
plt.subplot(1, 4, 3), plt.imshow(img_5, cmap='gray')
plt.subplot(1, 4, 4), plt.imshow(img_8, cmap='gray')
plt.show()
