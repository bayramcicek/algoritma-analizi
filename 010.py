#!/usr/bin/python3.6
# created by cicek on Mar 10, 2020 11:18


import random


def my_search(numbers, x):
    s = 0

    for i in numbers:
        s = s + 1

        if i == x:
            return True, s

    return False, s


numbers = [10, 13, 23, 310, 49]
x = 10
res = my_search(numbers, x)


print(res)


# def get_my_list(s):
#     list_1 = []
#     for i in range(s):
#         t = int(random.uniform(0, 1000))
#         list_1.append(t)
#     return list_1
#
#
# def get_my_number():
#     return int(random.uniform(0, 1000))
#
#
# my_list = get_my_list(10)
# my_number = get_my_number()
# print(my_list)
# print(my_number)
#
# res = my_search(my_list, my_number)[1]
# print(res)
#
#
# def my_seacrh_complexity(numOfItems=10, numOfTrials=5):
#     my_list = get_my_list(numOfItems)
#     my_search_numbers = get_my_list(numOfTrials)
#     # my_search_numbers = [2,45,78,-34,55] # buyult b n/2 ye yaklaşır
#
#     print("liste boyutu", len(my_list))
#     t = 0
#     for x in my_search_numbers:
#         t_1 = my_search(my_list, x)[1]
#         t = t + t_1
#     a, b = t, t / len(my_search_numbers)
#     print("ortalama deger", b)
#
#
# my_seacrh_complexity(10, 5)  # n --> n/2 çıktı
# my_seacrh_complexity(50, 25)
# my_seacrh_complexity(100, 50)
# my_seacrh_complexity(1000, 500)
# my_seacrh_complexity(1000, 800)
# my_seacrh_complexity(1000, 900)
