#!/usr/bin/python3
# created by cicek on Dec 13, 2020 3:31 PM

import numpy as np
import matplotlib.pyplot as plt


def display_two_image(im_1, im_2):
    plt.subplot(1, 2, 1)
    plt.imshow(im_1)

    plt.subplot(1, 2, 2)
    plt.imshow(im_2)
    plt.show()


# transpose
def rotate_by_i_j_swap(im_1):
    m, n, k = im_1.shape

    new_image = np.zeros((n, m, k), dtype='uint8')

    for i in range(m):
        for j in range(n):
            temp = im_1[i, j]
            new_image[j, i] = temp
    return new_image


# bir noktayı theta kadar yer değiştir
def rotate_one_point_w_theta_cclockwise(point, angle):
    """

    :param point: a pair of x, y indicating the location  of the pixel
    :param angle: angle in degrees
    :return:
    """

    theta = np.radians(angle)  # radyan'a çevirdik

    # dönüşüm matrisi
    r = np.array(((np.cos(theta), -np.sin(theta)),
                  (np.sin(theta), np.cos(theta))))

    v = np.array(point)

    # r matrisi ile v yi çarp,
    return r.dot(v).astype(int)


def get_all_new_location(im_1, angle):
    m, n, k = im_1.shape
    new_location_points = []

    for i in range(m):
        for j in range(n):
            new_location_points.append(rotate_one_point_w_theta_cclockwise([i, j], angle))

    return new_location_points


def get_min_max(new_location_points_):
    min_x, min_y = new_location_points_[0][0], new_location_points_[0][1]
    max_x, max_y = new_location_points_[0][0], new_location_points_[0][1]

    s1 = len(new_location_points_)
    for s in range(s1):
        if min_x > new_location_points_[s][0]:
            min_x = new_location_points_[s][0]

        if max_x > new_location_points_[s][0]:
            max_x = new_location_points_[s][0]

        if min_y > new_location_points_[s][1]:
            min_y = new_location_points_[s][1]

        if max_y > new_location_points_[s][1]:
            max_y = new_location_points_[s][1]

    return min_x, min_y, max_x, max_y


def rotate_an_image(im_1, angle):
    m, n, k = im_1.shape
    new_location_points = get_all_new_location(im_1, angle)
    min_x, min_y, max_x, max_y = get_min_max(new_location_points)

    new_m = max_x - min_x + 1
    new_n = max_y - min_y + 1

    x_offset = 0 - min_x
    y_offset = 0 - min_y

    new_image_2 = np.zeros((new_m, new_n, 3), dtype='uint8')
    for i in range(m):
        for j in range(n):
            new_i, new_j = rotate_one_point_w_theta_cclockwise([i, j], angle)
            new_image_2[new_i + x_offset, new_j + y_offset] = image_1[i, j]
    return new_image_2


image_1 = plt.imread('pic_1.jpg')

# image_2 = rotate_by_i_j_swap(image_1)
# image_3 = rotate_by_i_j_swap(image_2)
# display_two_image(image_1, image_2)

# new_location_points = get_all_new_location(image_1, 90)
# min_x, min_y, max_x, max_y = get_min_max(new_location_points)
# print(rotate_one_point_w_theta_cclockwise([1, 0], 90))

i_1 = rotate_an_image(image_1, 90)
plt.imshow(i_1)
plt.show()
