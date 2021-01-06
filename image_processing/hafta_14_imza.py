#!/usr/bin/python3
# created by cicek on Jan 06, 2021 11:27 AM

import matplotlib.pyplot as plt
import numpy as np
import os
from skimage.transform import resize

""" 
Multilayer Multi class perception, MBR resize
1) rgb -> bw
2) crop (imza atılan yeri merkeze almak) (Minimum bounding rectangle - MBR)
3) mxn -> fixed  
  
"""


def crop_and_return_min_mn_for_a_folder(folder_name):
    # for resize
    min_m_for_all, min_n_for_all = 0, 0
    files = get_all_files_in_folder(folder_name)
    i = 0
    for file in files:
        full_file_name = folder_name + "/" + file
        print(file, end=" ")
        # print(full_file_name)

        # noinspection PyBroadException
        try:
            im_rgb = plt.imread(full_file_name)
            im_bw = convert_rgb_to_bw(im_rgb)
            mbr = get_mbr_from_a_bw_image(im_bw)
            im_bw_cropped = crop_an_image_by_new_mn(im_bw, mbr)
            if i == 0:

                min_m_for_all, min_n_for_all = im_bw_cropped.shape
            else:
                if min_m_for_all > im_bw_cropped.shape[0]:
                    min_m_for_all = im_bw_cropped.shape[0]
                if min_n_for_all > im_bw_cropped.shape[1]:
                    min_n_for_all = im_bw_cropped.shape[1]

            new_file_name = file[0:-4] + "_cropped" + file[-4:]
            full_file_name = full_file_name + "/" + new_file_name
            plt.imsave(full_file_name, im_bw_cropped, cmap='gray')
            # print(new_file_name)

        except Exception:
            print("error in " + file)
    print(" finished ...")

    return min_m_for_all, min_n_for_all


# tüm klasörler
def get_all_folders_in_path(path_=""):
    my_folders = [folder for folder in os.listdir(path_) if os.path.isdir(path_ + '/' + str(folder))]
    return my_folders


# tüm dosyalar
def get_all_files_in_folder(path_=""):
    my_files = [file for file in os.listdir(path_) if os.path.isfile(path_ + '/' + str(file))]
    return my_files


def get_my_files(data_folder_1):
    files = get_all_files_in_folder(data_folder_1)
    return files


def get_mbr_from_a_bw_image(im_bw):
    # for smallest biggest m
    m, n = im_bw.shape[0], im_bw.shape[1]

    smallest_m = m

    biggest_m = 0

    for i in range(m):
        for j in range(n):
            intensity = im_bw[i, j]
            if intensity == 0 and i < smallest_m:
                smallest_m = i
            if intensity == 0 and i > biggest_m:
                biggest_m = i

    # for smallest biggest n
    smallest_n = n
    biggest_n = 0
    for i in range(m):
        for j in range(n):
            intensity = im_bw[i, j]
            if intensity == 0 and j < smallest_n:
                smallest_n = j
            if intensity == 0 and j > biggest_n:
                biggest_n = j
    # smallest_n, biggest_n
    # smallest_m, biggest_m

    m1, m2, n1, n2 = smallest_m, biggest_m, smallest_n, biggest_n

    return m1, m2, n1, n2


def crop_an_image_by_new_mn(im_bw, mbr):
    m1, m2, n1, n2 = mbr[0], mbr[1], mbr[2], mbr[3]

    # m, n = m2 - m1, n2 - n1
    my_new_image = im_bw[m1:m2 + 1, n1:n2 + 1]

    return my_new_image


def my_cropp_process():
    data_folder_1 = r"/home/cicek/Downloads/data_signature/160401002"
    files = get_my_files(data_folder_1)

    for file in files:
        full_file_name = data_folder_1 + "/" + file
        im_1 = plt.imread(full_file_name)
        # print(im_1.ndim, im_1.shape)  # 3 (200, 250, 3)
        im_2 = convert_rgb_to_bw(im_1)
        # print(im_2.ndim, im_2.shape)  # 2 (200, 200)
        mbr = get_mbr_from_a_bw_image(im_2)  # (53, 147, 40, 193)
        im_3 = crop_an_image_by_new_mn(im_2, mbr)
        # print(im_3.ndim, im_3.shape)  # 2 (95, 154)

        size = (200, 200)
        im_4 = resize(im_3, size)

        # plt.subplot(1, 3, 1), plt.imshow(im_1)
        # plt.subplot(1, 3, 2), plt.imshow(im_2, cmap='gray')
        # plt.subplot(1, 3, 3), plt.imshow(im_3, cmap='gray')
        # plt.show()

        a = file
        # a="1234567890.png"
        i = len(a) - 4
        b = a[0:-4] + "_cropped_" + a[i:]
        print(a)
        print(b)
        full_file_name = data_folder_1 + "/" + b
        # full_file_name

        plt.imsave(full_file_name, im_4, cmap='gray')


def convert_rgb_to_bw(im_rbg):
    im_rbg = im_rbg / np.max(im_rbg)
    # m,n,k=im_rbg.shape
    m = im_rbg.shape[0]
    n = im_rbg.shape[1]

    my_new_image = np.zeros((m, n), dtype=int)
    my_new_image = my_new_image + 1

    for row in range(m):
        for column in range(n):

            s = im_rbg[row, column, 0] / 3 + im_rbg[row, column, 1] / 3 + im_rbg[row, column, 2] / 3

            diff_to_0 = s - 0
            diff_to_1 = np.abs(1 - diff_to_0)

            if diff_to_0 < diff_to_1:
                my_new_image[row, column] = 0
            else:
                my_new_image[row, column] = 1

    return my_new_image


my_cropp_process()

"""
160401002_08.png
160401002_08_cropped_.png
160401002_20.png
160401002_20_cropped_.png
160401002_13.png
160401002_13_cropped_.png
160401002_15.png
160401002_15_cropped_.png
160401002_09.png
160401002_09_cropped_.png
160401002_06.png
160401002_06_cropped_.png
160401002_28.png
160401002_28_cropped_.png
160401002_01.png
160401002_01_cropped_.png
160401002_14.png
160401002_14_cropped_.png
160401002_17.png
160401002_17_cropped_.png
160401002_26.png
160401002_26_cropped_.png
160401002_16.png
160401002_16_cropped_.png
160401002_30.png
160401002_30_cropped_.png
160401002_test.png
160401002_test_cropped_.png
160401002_24.png
160401002_24_cropped_.png
160401002_02.png
160401002_02_cropped_.png
160401002_21.png
160401002_21_cropped_.png
160401002_23.png
160401002_23_cropped_.png
160401002_25.png
160401002_25_cropped_.png
160401002_11.png
160401002_11_cropped_.png
160401002_04.png
160401002_04_cropped_.png
160401002_29.png
160401002_29_cropped_.png
160401002_18.png
160401002_18_cropped_.png
160401002_03.png
160401002_03_cropped_.png
160401002_19.png
160401002_19_cropped_.png
160401002_27.png
160401002_27_cropped_.png
160401002_05.png
160401002_05_cropped_.png
160401002_07.png
160401002_07_cropped_.png
160401002_10.png
160401002_10_cropped_.png
160401002_22.png
160401002_22_cropped_.png
160401002_12.png
160401002_12_cropped_.png

Process finished with exit code 0

"""
