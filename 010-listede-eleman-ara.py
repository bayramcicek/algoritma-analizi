#!/usr/bin/python3.6
# created by cicek on Mar 10, 2020 11:18

import random


def search_number(list, number):  # listede eleman ara
    counter = 0

    for i in list:
        counter = counter + 1

        if i == number:
            return True, counter

    return False, counter


# list = [10, 13, 23, 310, 49]
#
# number = 310  # bu değeri değiştirerek dene
# print(search_number(list, number))  # (True, 4)
#
# """
# search_number(list, number) için:
#
# best_case -> O(1) (True)
# average_case -> O(n) (True)
# worst_case -> O(n) (False)
#
# """


def generate_list(limit):
    list = []

    for i in range(limit):
        t = int(random.uniform(0, 1000))
        list.append(t)

    return list


def get_random_number():
    return int(random.uniform(0, 1000))


def search_complexity(num_of_items, num_of_trials):
    list = generate_list(num_of_items)
    arama_sayilari = generate_list(num_of_trials)
    # arama_sayilari = [2, 45, 78, -34, 55]  # listeyi büyült. ortalama n/2 ye yaklaşır

    print("\nliste boyutu:", len(list))
    counter = 0

    for i in arama_sayilari:
        t = search_number(list, i)[1]  # counter atanıyor
        counter = counter + t

    ortalama = counter / len(arama_sayilari)

    print("ortalama:\t ", ortalama)


# # list = generate_list(10)
# # number = get_random_number()
# #
# # print(list)
# # print("number:", number)
# #
# # # result = search_number(list, number)[1]
# # result = search_number(list, number)
# # print("search result:", result)
# #
# # """
# # [688, 989, 873, 649, 985, 989, 914, 421, 486, 841]
# # number: 421
# # search result: (True, 8)
# #
# # [709, 978, 91, 901, 101, 723, 104, 914, 432, 590]
# # number: 128
# # search result: (False, 10)
# #
# # """
#
# search_complexity(10, 5)
# search_complexity(50, 25)
# search_complexity(100, 50)
# search_complexity(1000, 500)
# search_complexity(1000, 800)
# search_complexity(1000, 1000)  # n --> n/2. ortalama, liste boyutunun yarısına yaklaştı
#
# """
# liste boyutu: 10
# ortalama:	  10.0
#
# liste boyutu: 50
# ortalama:	  48.72
#
# liste boyutu: 100
# ortalama:	  95.94
#
# liste boyutu: 1000
# ortalama:	  620.654
#
# liste boyutu: 1000
# ortalama:	  642.1
#
# liste boyutu: 1000
# ortalama:	  655.029
#
# """

search_complexity(1000, 5)
search_complexity(1000, 25)
search_complexity(1000, 50)
search_complexity(1000, 100)
search_complexity(1000, 250)
search_complexity(1000, 350)
search_complexity(1000, 500)
search_complexity(1000, 800)
search_complexity(1000, 1000)

"""
liste boyutu: 1000
ortalama:	  924.0

liste boyutu: 1000
ortalama:	  804.48

liste boyutu: 1000
ortalama:	  664.62

liste boyutu: 1000
ortalama:	  679.39

liste boyutu: 1000
ortalama:	  621.768

liste boyutu: 1000
ortalama:	  606.9971428571429

liste boyutu: 1000
ortalama:	  676.892

liste boyutu: 1000
ortalama:	  647.28625

liste boyutu: 1000
ortalama:	  632.968
"""
