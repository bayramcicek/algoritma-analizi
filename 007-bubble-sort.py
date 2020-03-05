#!/usr/bin/python3.6
# created by cicek on Mar 05, 2020 15:35


def bubble_sort(list):
    n = len(list)

    for i in range(n - 1, -1, -1):

        for j in range(0, i):

            if list[j] > list[j + 1]:
                temp = list[j + 1]
                list[j + 1] = list[j]
                list[j] = temp

    return list


list = [2, 4, -5, -2, 9, 1, 6]
print(list, "len: ", len(list), "\n")

result = bubble_sort(list)
print(result)
# bubble_sort(list)
# Q(n^2)
