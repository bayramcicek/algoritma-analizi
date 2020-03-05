#!/usr/bin/python3.6
# created by cicek on Mar 03, 2020 14:52


def insertion_sort(list):
    n = len(list)
    loop_counter = 0

    for i in range(1, n):
        key = list[i]
        j = i - 1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
            loop_counter = loop_counter + 1

        list[j + 1] = key

    return list, loop_counter


list = [2, 1, 6, -2, 4, 9, -5]

list, loop_counter = insertion_sort(list)
print(list, "\ndöngü:", loop_counter)

# [2, 1, 6, -2, 4, 9, -5] --> sıralı gönder,  döngü: 11 -> döngü: 0 olur
