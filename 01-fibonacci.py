#!/usr/bin/python3.6
# created by cicek on Mar 03, 2020 16:35

counter = 0


def fib_2(n):
    global counter
    if n < 2:
        counter += 1
        return n
    else:
        a = 0
        b = 1
        c = a + b
        s = 1
        while (s < n):
            c = a + b
            a = b
            b = c
            s += 1
            counter += 1
        return c


n = 10
result = fib_2(n)
print(result)
# print(counter)
'''
fib <-  n   -> counter
0       00  -> 1
1       01  -> 1
1       02  -> 1
2       03  -> 2
3       04  -> 3
5       05  -> 4
8       06  -> 5
13      07  -> 6
21      08  -> 7
.       09  -> 8
.       10  -> 9
.       11  -> 10
        12  -> 11
        13  -> 12

karmaşıklık -> O(n)
'''
