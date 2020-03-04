#!/usr/bin/python3.6
# created by cicek on Mar 03, 2020 21:00


# a^b 'yi bulan fonksiyon karmaşıklığı
counter = 0


def fun1(a, b):
    global counter
    s = 1

    for i in range(b):
        s = s * a
        counter += 1

    return s


a, b = 2, 16
result = fun1(a, b)

# print(result)
print(counter)  # b ne ise o kadar çalışıyor -->  O(n)
