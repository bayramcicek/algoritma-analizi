#!/usr/bin/python3
# created by cicek on May 04, 2020 15:58

'''
Heapsort:   ağacın ilk elemanını açığa al.
            son elemanı ilk eleman yap.
            min_heap uygula.
            tekrarla...
O(nlogn)
'''


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


def heapsort(array):
    array = array.copy()  # pointer'a değil kopyasına ihtiyaç var
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array


my_array_min_heap = [8, 10, 3, 4, 7, 15, 1, 2, 16]
my_array_sorted = heapsort(my_array_min_heap)
print(my_array_sorted)  # [1, 2, 3, 4, 7, 8, 10, 15, 16]
