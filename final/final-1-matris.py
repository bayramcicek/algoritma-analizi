#!/usr/bin/python3
# created by cicek on Jun 10, 2020 12:55

import random
from enum import Enum


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

islem_sayisi = 0
""" 1.c) mxn matrisini 'kare matris' olarak ele alırsak;

aşağıda görüldüğü gibi karmaşıklığı deneysel olarak ölçtüğümüzde
karmaşıklığı yaklaşık -> O(m x (n-10) x ((n-10)/2)) buluruz:

12x12 -> islem_sayisi = 72      kaba sonuc = 24
14x14 -> islem_sayisi = 210     kaba sonuc = 112
16x16 -> islem_sayisi = 448     kaba sonuc = 288
18x18 -> islem_sayisi = 810     kaba sonuc = 576
20x20 -> islem_sayisi = 1320    kaba sonuc = 1000
22x22 -> islem_sayisi = 2002    kaba sonuc = 1584
24x24 -> islem_sayisi = 2880    kaba sonuc = 2352 """
def palindrom_bul():
    global islem_sayisi
    palindrom_sayisi = 0

    # her satırda kontrol edilecek.
    for satir in range(len(list)):

        '''10 ve daha fazla kelime palindrom mu kontrolü.
        her sütuna bakılacak'''
        for sınır in range(10, len(list[0]) + 1):
            baslangic = 0

            # satır sonuna geldi mi kontrolü.
            while (sınır != len(list[0]) + 1):

                # polindrom kontrolü
                word = "".join(list[satir][baslangic:sınır])
                palindrom = str(word) == str(word)[::-1]

                islem_sayisi += 1
                # palindrom bulundu ise yazdır.
                if (palindrom == True):
                    palindrom_sayisi += 1
                    print(palindrom, word)

                baslangic += 1
                sınır += 1

    print("palindrom sayısı ->", palindrom_sayisi)


list = []


# fonksiyon tek sefer çalışır. karmaşıklık -> O(1)
def abc_test_et():
    global list

    # 1.a) 2 boyutlu liste oluştur.
    list = matris_2d(20, 20)
    print("--liste ilk hali--\n", list)

    # 1.b) kelimeyi aktar.
    word_aktar(7, 2, 'ZTKAYAKKAYAKTZ', 0)
    print("--liste SON hali--\n", list, "\n")

    # 1.c) palindrom bul.
    palindrom_bul()
    print("işlem =", islem_sayisi)


# 1.d) test fonksiyonu.
abc_test_et()

""" çıktı:
...
...
True KAYAKKAYAK
True TKAYAKKAYAKT
True ZTKAYAKKAYAKTZ
palindrom sayısı -> 3
işlem = 1320 """
