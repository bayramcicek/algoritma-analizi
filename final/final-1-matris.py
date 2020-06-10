#!/usr/bin/python3
# created by cicek on Jun 10, 2020 12:55

import random

"""
1.a) satır(m) sütün(n) sayısını parametre olarak alıp,
her bir elemanı bir harf olan mxn lik iki boyutlu matris
oluşturup ve bunu return eden fonksiyon yazınız, karmaşıklığını bulunuz.
Elemanlar random olarak belirlenecektir.
"""


def matris(m, n):
    rows = m
    cols = n
    letters = 'abcdefghijklmnopqrstuvwxyz'

    # listeyi başlat
    list_2d = [['0'] * cols for _ in range(rows)]

    # listeye rastgele harf ata
    for i in range(rows):
        for k in range(cols):
            list_2d[i][k] = letters[(random.randint(0, 25))]

    return list_2d


print(matris(5, 5))
