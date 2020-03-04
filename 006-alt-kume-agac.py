#!/usr/bin/python3.6
# created by cicek on Mar 04, 2020 16:19


def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b


def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))


def alt_kume_agac(list):
    n = len(list)

    if n == 1:
        return list[0]
    else:
        left_list = list[0:(n // 2)]
        right_list = list[(n // 2):n]

        left_sum = alt_kume_agac(left_list)
        right_sum = alt_kume_agac(right_list)

        center_sum = 0
        temp_sum_left = 0
        t = 0

        for i in range((n // 2) - 1, -1, -1):
            t = t + list[i]

            if t > temp_sum_left:
                temp_sum_left = t

        temp_sum_right = 0
        t = 0

        for i in range((n // 2), n):
            t = t + list[i]

            if t > temp_sum_right:
                temp_sum_right = t

        center_sum = temp_sum_left + temp_sum_right

        return max_of_three(left_sum, right_sum, center_sum)


list = [4, -3, 5, -2, -1, 2, 6, -2]

result = alt_kume_agac(list)
print(result)  # 11
