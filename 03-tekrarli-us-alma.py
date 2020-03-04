#!/usr/bin/python3.6
# created by cicek on Mar 04, 2020 09:40


counter = 0


def power_recursive(a, b):
    global counter
    counter += 1

    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return power_recursive(a, b - 1) * a


a, b = 2, 7
result = power_recursive(a, b)

# print(result)
print(counter)

'''
b       counter     
0       1           
1       1         
2       2           
3       3           
4       4           
5       5              
6       6           
7       7           

karmaşıklık --> O(n)

'''
