#!/usr/bin/python3.6
# created by cicek on Apr 17, 2020 16:29

import random
import matplotlib.pyplot as plt

'''
Bayram Çiçek - 160401002 - binary search empiric study

Due April 17 at 11:59 PM
konu: week_3_deneysel analiz uygulaması linear/binary search

Hafta 3 için yüklenen video lardaki kodu kendi bilgisayarınızda yazıp,
çalıştırıp tecrübe edininiz, son halini github hesabınıza upload ediniz.

'''

'''
binary search karmaşıklık -> logn
'''


def my_binary_search(my_list, item_search):
    found = (-1, -1, 0)  # 0 -> kaç defa arama yaptı
    low = 0
    high = len(my_list) - 1
    s = 0

    while low <= high:
        mid = (low + high) // 2
        print(low, high, mid)
        s = s + 1

        if my_list[mid] == item_search:
            return my_list[mid], mid, s
        elif my_list[mid] > item_search:
            high = mid - 1
        else:
            low = mid + 1

    print(s)
    return found[0], found[1], s
    # None


def my_bubble_sort(my_list):
    n = len(my_list)
    # print(my_list)

    for i in range(n - 1, -1, -1):

        for j in range(0, i):

            if not (my_list[j] < my_list[j + 1]):
                # print("swap işlemi")
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp

    return my_list


def get_n_random_numbers(n=10, min_=-5, max_=5):
    numbers = []

    for i in range(n):
        numbers.append(random.randint(min_, max_))
    return numbers


def my_experimental_study_binary(iter_num=50):
    x_low = -100
    x_high = 100
    array_size = 40

    print("array size: ", array_size)

    cost = []
    for iter in range(iter_num):
        my_list = get_n_random_numbers(array_size, x_low, x_high)
        my_list = my_bubble_sort(my_list)

        search_item = get_n_random_numbers(1, x_low, x_high)
        search_item = search_item[0]

        result = my_binary_search(my_list, search_item)
        cost.append(result[2])

        # if result[1] == -1:
        #     cost.append(array_size)
        # else:
        #     cost.append(result[1])
        # print(result)

    return cost


x_low = -10
x_high = 10
array_size = 4

# my_list = get_n_random_numbers(array_size, x_low, x_high)
# print(my_list)  # [-5, -10, -1, -6]
#
# my_list = my_bubble_sort(my_list)
# print(my_list)  # [-10, -6, -5, -1]
#
# search_item = get_n_random_numbers(1, x_low, x_high)
# search_item = search_item[0]
# print(search_item, "\n")
#
# print(my_binary_search(my_list, search_item))
# '''
# çıktı:
# [1, -3, 6, -2]
# [-3, -2, 1, 6]
# -2
#
# 0 3 1
# (-2, 1, 1)
# '''

res = my_experimental_study_binary()
print(res)
'''
çıktı:

...
...
...

5
0 39 19
0 18 9
0 8 4
5 8 6
7 8 7
8 8 8
6
0 39 19
20 39 29
30 39 34
35 39 37
35 36 35
36 36 36
6

[6, 5, 5, 5, 5, 6, 3, 5, 6, 6, 6, 5, 6, 5, 5, 5, 6, 6, 5, 6, 5, 5, 3, 6, 5, 5, 6, 5, 6,
2, 6, 6, 5, 5, 5, 5, 6, 6, 5, 6, 5, 6, 5, 6, 6, 5, 5, 5, 6, 6]

Process finished with exit code 0

'''

plt.plot(res)

# sudo apt install python3-tk (grafiğin gösterilmesi için indir)
plt.show()  # Figure_2_binary.png
