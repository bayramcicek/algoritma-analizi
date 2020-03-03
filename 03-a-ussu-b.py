#!/usr/bin/python3.6
# created by cicek on Mar 03, 2020 21:17

# 4^6  --> (4*4)^3 olarak yazılırsa:
counter = 0


def fun2(a, b):
    global counter
    counter += 1
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return fun2(a * a, b / 2)


a, b = 2, 16 # b --> 2, 4, 8, 16, 32, 64 ... atayınız
result = fun2(a, b)
# print(result)
print(counter)
'''
b       counter     log(b) (2 tabanında)
0       1           - 
1       1           0
2       2           1
4       3           2
8       4           3
16      5           4   
32      6           5
64      7           6



'''