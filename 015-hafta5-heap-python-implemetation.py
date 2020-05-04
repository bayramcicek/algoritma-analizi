#!/usr/bin/python3
# created by cicek on May 03, 2020 21:35

def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)


def build_min_heap(array):
    for i in reversed(range(len(array) // 2)):
        min_heapify(array, i)


my_array_min_heap = [8, 10, 3, 4, 7, 15, 1, 2, 16]

build_min_heap(my_array_min_heap)
print(my_array_min_heap)  # [1, 2, 3, 4, 7, 15, 8, 10, 16]
