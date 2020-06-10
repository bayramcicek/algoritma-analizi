#!/usr/bin/python3
# created by cicek on Jun 10, 2020 12:55

import random
from enum import Enum

"""
1.c) Elemanları harflerden oluşan bir matrisde ->( soldan sağa) ,
<- (soldan sağa ) yönlerinde uzunluğu 10 veya daha fazla olan bütün 
palindromları ( palindrom: tersten okunuşu ile aynı olan kelime; 
mum,kapak,nazan, yapay … )  bulan bir fonksiyon yazınız, 
karmaşıklığını bulunuz.

"""


class Orientation(Enum):
    SOL_SAG = 0
    SAG_SOL = 1
    A_YUKARI = 2
    Y_ASAGI = 3


""" 1.a) iç içe olan for döngülerinden;
dışta olan n defa, iç kısımda olan n defa çalışacağından
-> toplam karmaşıklık -> yaklaşık O(n^2) olur. """


def matris_2d(m, n):
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


""" 1.b) koşul durumlarından sadece 1 tanesine girecektir.
bu koşulların içinde ise sadece 1 tane for döngüsü var ve
bu döngüler my_word uzunluğu kadar çalışacağından
toplam karmaşıklık -> yaklaşık O(n) olur. """


def word_aktar(satir, sutun, my_word, orientation):
    # orientation == 0 ise soldan sağa yerleştir.
    if (Orientation.SOL_SAG.value == orientation):
        # my_word'u belirtilen indexten itibaren yerleştir.
        for i in range(len(my_word)):
            list[satir][sutun] = my_word[i]
            sutun += 1
            if (sutun == len(list[0])):
                sutun = 0

    # orientation == 1 ise sağdan sola yerleştir.
    elif (Orientation.SAG_SOL.value == orientation):
        # my_word'u belirtilen indexten itibaren yerleştir.
        for i in range(len(my_word)):
            list[satir][sutun] = my_word[i]
            sutun -= 1
            if (sutun == -1):
                sutun = len(list[0]) - 1

    # orientation == 2 ise aşağıdan yukarıya yerleştir.
    elif (Orientation.A_YUKARI.value == orientation):
        # my_word'u belirtilen indexten itibaren yerleştir.
        for i in range(len(my_word)):
            list[satir][sutun] = my_word[i]
            satir -= 1
            if (satir == -1):
                satir = len(list) - 1

    # orientation == 3 ise yukarıdan aşağıya yerleştir.
    elif (Orientation.Y_ASAGI.value == orientation):
        # my_word'u belirtilen indexten itibaren yerleştir.
        for i in range(len(my_word)):
            list[satir][sutun] = my_word[i]
            satir += 1
            if (satir == len(list)):
                satir = 0

    else:
        print("\nHatalı yön girdiniz...\n")

# 2 boyutlu liste oluştur.
list = matris_2d(10, 10)
print("--liste ilk hali--\n", list)

word_aktar(2, 1, 'BAYRAM', 0)
print("--liste SON hali--\n", list)
