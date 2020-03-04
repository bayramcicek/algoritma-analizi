#!/usr/bin/python3.6
# created by cicek on Mar 03, 2020 14:48


counter = 0


def fib_1(n):
    # print(n)
    global counter
    counter += 1

    if n < 2:
        return n

    else:
        return (fib_1(n - 1)) + (fib_1(n - 2))


n = 10  # kaçıncı sıradaki fib sayısı -> 1 1 2 3 5 8 13...
result = fib_1(n)

print(result)
# print(counter)

'''
fib <-  n   -> counter
0       00  -> 1 
1       01  -> 1
1       02  -> 3
2       03  -> 5
3       04  -> 9
5       05  -> 15
8       06  -> 25
.       07  -> 41
.       08  -> 67
        09  -> 109
        10  -> 177
        11  -> 287
        12  -> 465
        13  -> 753
        
        karmaşıklık -> O(2^n)
'''
