#!/usr/bin/python3.6
# created by cicek on Apr 12, 2020 10:07

'''
We basically ignore half of the elements just after one comparison.
- Compare x with the middle element.
- If x matches with middle element, we return the mid index.
- Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element.
  So we recur for right half.
- Else (x is smaller) recur for the left half.
https://www.geeksforgeeks.org/binary-search/
'''


# Python3 code to implement iterative Binary Search.

# It returns location of x in given array arr if present, else returns -1
def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2
        print(arr[mid])

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element was not present
    return -1


# Test Code
arr = [100, 50, 40, 60, 120, 110, 130, 20, 45, 55, 61, 105, 115, 125, 140]
x = 125

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
