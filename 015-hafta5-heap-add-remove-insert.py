#!/usr/bin/python3
# created by cicek on May 04, 2020 21:42

# for n in range(10):
#     if (n // 2 == n / 2):
#         parent = (n // 2) - 1
#     else:
#         parent = (n // 2)
#
#     print(n, parent)
# '''
# 0 -1
# 1 0
# 2 0
# 3 1
# 4 1
# 5 2
# 6 2
# 7 3
# 8 3
# 9 4
# '''


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


def insertItemToHeap(my_heap, item):
    my_heap.append(item)
    n = len(my_heap) - 1

    if (n // 2 == n / 2):
        parent_indis = n // 2 - 1
    else:
        parent_indis = n // 2

    print("n, parent indis:", n, parent_indis)

    while parent_indis >= 0:
        print("parent indis: ", parent_indis)
        min_heapify(my_heap, parent_indis)
        # if exchange not exists, then break
        if (parent_indis // 2 == parent_indis / 2):
            parent_indis = parent_indis // 2 - 1
        else:
            parent_indis = parent_indis // 2
    return my_heap


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
    return array


def heapsort(array):
    array = array.copy()  # pointer'a değil kopyasına ihtiyaç var
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array


def removeItemFromHeap(my_heap):
    my_heap[0], my_heap[-1] = my_heap[-1], my_heap[0]
    my_heap.pop()
    min_heapify(my_heap, 0)

    return my_heap


# array_1 = [8, 10, 3, 4, 7, 15, 1, 2, 16]
# array_2 = build_min_heap(array_1)

array_1 = [8, 10, 3, 4, 7, 15]
print(array_1)

array_2 = build_min_heap(array_1)
print(array_2)

insertItemToHeap(array_2, 5)
print(array_2)

'''
[8, 10, 3, 4, 7, 15]
[3, 4, 8, 10, 7, 15]
n, parent indis: 6 2
parent indis:  2
parent indis:  0
[3, 4, 5, 10, 7, 15, 8]

Process finished with exit code 0

'''

remove_array_1 = [1, 3, 5, 4, 7, 15, 8, 12, 10]
print(remove_array_1)
removeItemFromHeap(remove_array_1)
print(remove_array_1)

'''
[1, 3, 5, 4, 7, 15, 8, 12, 10]
[3, 4, 5, 10, 7, 15, 8, 12]
base case logn
'''
