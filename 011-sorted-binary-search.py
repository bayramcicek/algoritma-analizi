#!/usr/bin/python3.6
# created by cicek on Apr 07, 2020 11:54

def my_binary_search(my_list, item_search):
    found = (-1, -1)
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        print(my_list[mid])

        if my_list[mid] == item_search:
            return my_list[mid], mid
        elif my_list[mid] > item_search:
            high = mid - 1
        else:
            low = mid + 1

    return found  # None


# sıralı liste olmalı
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
print(my_binary_search(list, 80))

'''
output:

60
90
70
80
(80, 7)

Process finished with exit code 0
'''
