#!/usr/bin/python3.6
# created by cicek on Mar 04, 2020 11:52


def subset(list):
    n = len(list)
    max_sum = 0

    for i in range(n):

        for j in range(i, n):
            t = 0

            for k in range(i, j + 1):
                t = t + list[k]

            if t > max_sum:
                max_sum = t

    return max_sum


def liste_eleman_toplami(list):
    n = len(list)
    max_sum = 0

    for i in range(n):
        t = 0

        for k in range(i, n):
            t = t + list[k]

        if t > max_sum:
            max_sum = t

    return max_sum


list = [4, -3, 5, -2, -1, 2, 6, -2]

sum_result = liste_eleman_toplami(list)
sub_result = subset(list)

print(sum_result)  # 9
print(sub_result)  # 11
