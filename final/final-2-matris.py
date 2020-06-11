#!/usr/bin/python3
# created by cicek on Jun 11, 2020 01:48

import random

"""


"""

''' 1.a)    Bu fonksiyonun karmaşıklığı for döngüsü için O(n),
append() için O(1)'dir. -> toplam karmaşıklık -> yaklaşık O(n) olur.
fakat amortized cost'ta, sistemin n operasyonda
bir defa worst case'e girmesi ile append() 
karmaşıklığı -> O(n) olur. Bu da toplam karmaşıklığı
append()'in worst case'e girdiği durumlarda -> O(n^2) yapar. '''


def vektor_olustur(n):
    # vektörü başlat.
    vektor_list = []

    # n elemanlı vektör için döngü.
    for i in range(n):
        # rastgele ekle.
        vektor_list.append(random.randint(0, n))

    return vektor_list


''' 1.b)    Bu fonksiyonda else kısmındaki for döngüsüne 
girildiğinde for döngüsü verktör uzunluğu kadar çalışacaktır.
Bu yüzden karmaşıklık yaklaşık -> O(n) olur.'''


def skaler_carp(vektor_1, vektor_2):
    sonuc = 0
    # vektörler aynı boyutta değilse uyarı ver.
    if (len(vektor_1) != len(vektor_2)):
        print("vektörler aynı boyutta olmalıdır.")
    else:
        """vektör boyutu kadar aynı indexteki her 
        elemanları çarp ve en sonunda topla."""
        for i in range(len(vektor_1)):
            sonuc += vektor_1[i] * vektor_2[i]
    return sonuc

""" 1.c)    """
def matris_olustur(m, n):


def test():
    # 1.a) vektor_olustur(n)
    print(vektor_olustur(10))

    # 1.b) skaler çarpım.
    a = vektor_olustur(4)
    b = vektor_olustur(4)
    print(skaler_carp(a, b))


test()
