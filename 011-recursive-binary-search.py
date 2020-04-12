#!/usr/bin/python3.6
# created by cicek on Apr 12, 2020 07:59

'''
We basically ignore half of the elements just after one comparison.
- Compare x with the middle element.
- If x matches with middle element, we return the mid index.
- Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element.
  So we recur for right half.
- Else (x is smaller) recur for the left half.
https://www.geeksforgeeks.org/binary-search/
'''


# Python3 Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + ((r - l) // 2)
        print(arr[mid])

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it an only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
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
