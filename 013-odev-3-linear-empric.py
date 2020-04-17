#!/usr/bin/python3.6
# created by cicek on Apr 16, 2020 18:03

import random
import matplotlib.pyplot as plt

'''
Bayram Çiçek - 160401002

Due April 17 at 11:59 PM
konu: week_3_deneysel analiz uygulaması linear/binary search

Hafta 3 için yüklenen video lardaki kodu kendi bilgisayarınızda yazıp,
çalıştırıp tecrübe edininiz, son halini github hesabınıza upload ediniz.

'''

'''
lineer aramanın base case'i yoktur. hafızaya aldığı en son şeyi geri yolar.
en son elemanı bulmak istiyorsak mutlaka break konulmalı.
break koyunca karmaşıklık değişti. 

linear search karmaşıklık -> n


'''


def get_n_random_numbers(n=10, min_=-5, max_=5):
    numbers = []

    for i in range(n):
        numbers.append(random.randint(min_, max_))
    return numbers


# my_list = get_n_random_numbers()
# print(my_list)


def my_linear_search(my_list, item_search):
    found = (-1, -1)  # default, eğer listede yoksa
    n = len(my_list)
    for indis in range(n):

        if my_list[indis] == item_search:
            found = (my_list[indis], indis)  # listede bulundu, return bulunn sayı, indisi
            break  # uncomment for last found
    return found


# result = my_linear_search(my_list, -2)
# print(result)
#
# '''
# çıktı:
#
# [-4, -1, 3, 5, -2, -5, 4, 0, -5, -2]
# (-2, 9)
#
# Process finished with exit code 0
# '''

def my_experimental_study(iter_num=50):
    x_low = -100
    x_high = 100
    array_size = 40

    print("array size: ", array_size)

    cost = []
    for iter in range(iter_num):
        my_list = get_n_random_numbers(array_size, x_low, x_high)
        search_item = get_n_random_numbers(1, x_low, x_high)
        search_item = search_item[0]

        result = my_linear_search(my_list, search_item)

        if result[1] == -1:
            cost.append(array_size)
        else:
            cost.append(result[1])
        print(result)

    return cost


res = my_experimental_study()
print(res)

'''
çıktı:

array size:  40
(-1, -1)
(-85, 16)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-36, 13)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-86, 30)
(-1, -1)
(46, 34)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(5, 31)
(-1, -1)
(-53, 3)
(-1, -1)
(-1, -1)
(-1, -1)
(47, 2)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
(-1, -1)
[40, 16, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 13, 40, 40, 40, 40, 40, 40, 40, 40,
40, 40, 30, 40, 34, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 31, 40, 3, 40, 40, 40, 2, 40,
40, 40, 40, 40]

Process finished with exit code 0

'''
plt.plot(res)

# sudo apt install python3-tk (grafiğin gösterilmesi için indir)
plt.show()  # Figure_1.png
