#!/usr/bin/python3
# created by cicek on Jun 11, 2020 01:48 - (Bayram Çiçek - 160401002)

import random

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


""" 1.c)    for döngüsü m kadar çalışır. bu yüzden 
toplam karmaşıklık O(n)'dir. Fakat append() amortised
cost bakımından en az 1 defa worst case'te girer. 
Amortised cost için for döngüsünü de katar isek 
worst case n*n'den -> O(n^2) olur. """
def matris_olustur(m, n):
    list = []
    # m -> satır olduğu için m kadar döngüde kalacak.
    for i in range(m):
        # n boyutlu liste oluşturup list'e ekleyecek.
        list.append(vektor_olustur(n))

    return list


""" 1.d)    karmaşıklık çarpılan matrislerin
satır ve sütun sayısına bağlıdır. 3 adet iç içe for
döngüsü karmaşıklığı arttırır. axb * bxc işleminde
karmaşıklık -> O(b*c*a) olur. Çarpılan matrislerin kare
matris ve aynı satır ve sütun sayısına sahip olduğunu kabul edersek
(worst case) karmaşıklık yaklaşık -> O(n^3) bulunur. """
def iki_matris_carp(matris_1, matris_2):
    # matris_1 sütunu ile matris_2 satırı eşit mi kontrolü.
    if (len(matris_1[0]) != len(matris_2)):
        print("1. matris sütunu ile "
              "2. matris satır uzunluğu eşit olmalıdır.")

    # çarpma işlemi -> axb * bxc = axc
    else:
        """çarpma sonucunu yazacağımız carpma_sonuc matrisini oluştur.
        carpma_sonuc matrisinin;
        satır uzunluğu -> ilk matrisin satır uzunluğu
        sütun uzunluğu -> ikinci matrisin sütun uzunluğu kadardır."""
        carpma_sonuc = [[0] * len(matris_2[0]) for _ in range(len(matris_1))]

        # matris_1 'in satırı uzunluğuna döngü.
        for i in range(len(matris_1)):
            # matris_2 'in sütunu uzunluğuna döngü.
            for j in range(len(matris_2[0])):
                # matris_2 'in satırı uzunluğuna döngü.
                for k in range(len(matris_2)):
                    carpma_sonuc[i][j] += matris_1[i][k] * matris_2[k][j]

        return carpma_sonuc


""" 1.d)    Bu fonksiyon sadece 1 defa çalışır fakat 
içeride kullanılan fonksiyonlarıı da ele alırsak 
karmaşıklık, 4 tane iki_matris_carp() fonksiyonu
kullanıldığı için yaklaşık -> O( 4*(n^3) ) olacaktır. """
def bes_matris_carp(m1, m2, m3, m4, m5):
    result = iki_matris_carp(m1, m2)
    result = iki_matris_carp(result, m3)
    result = iki_matris_carp(result, m4)
    result = iki_matris_carp(result, m5)
    return result


""" test() fonksiyonu. içindeki çalışan fonksiyonları göz ardı edersek
karmaşıklık O(1) 'dir. """
def test():
    # 1.a) vektor_olustur(n)
    vektor = vektor_olustur(10)
    # print(vektor)

    # 1.b) skaler çarpım.
    a = vektor_olustur(4)
    b = vektor_olustur(4)
    skaler = skaler_carp(a, b)
    # print(skaler)

    # 1.c) matris oluştur.
    matris = matris_olustur(6, 6)
    # print(matris)

    # 1.d) 2 matris çarp.
    """matrisler axb * bxc = axc olmalıdır. yani ilk matrisin
    sütunu ile ikinci matrisin satırı eşit olmalıdır."""
    c = matris_olustur(2, 3)
    d = matris_olustur(3, 4)
    # print("c matrisi\n", c)
    # print("d matrisi\n", d)
    carp = iki_matris_carp(c, d)
    # print("carpma_sonuc \n", carp)
    """çıktı:
    c matrisi
     [[2, 2, 2],
     [3, 1, 0]]
    d matrisi
     [[0, 1, 4, 4],
     [3, 0, 1, 4],
     [2, 3, 3, 2]]
    carpma_sonuc 
     [[10, 8, 16, 20],
     [3, 3, 13, 16]]
     """

    # 1.e) 5 matris çarpımı.
    """ matrisler kolaylık açısından kare matris ve
    aynı satır-sütun uzunluğuna sahip olmalıdır. """
    m1 = matris_olustur(5, 5)
    m2 = matris_olustur(5, 5)
    m3 = matris_olustur(5, 5)
    m4 = matris_olustur(5, 5)
    m5 = matris_olustur(5, 5)
    print("m1\n", m1)
    print("m2\n", m2)
    print("m3\n", m3)
    print("m4\n", m4)
    print("m5\n", m5)
    bes = bes_matris_carp(m1, m2, m3, m4, m5)
    print("bes matris carpimi\n", bes)
    """
    m1
     [[1, 3, 2],
     [0, 1, 2],
     [0, 3, 1]]
    m2
     [[1, 1, 1],
     [1, 1, 3],
     [1, 3, 3]]
    m3
     [[1, 2, 0],    
     [2, 0, 0],
     [1, 2, 2]]
    m4
     [[1, 1, 3],    
     [3, 1, 3],
     [2, 2, 1]]
    m5
     [[3, 2, 1],
     [0, 0, 0],
     [2, 3, 0]]
     bes matris carpimi
    [[1294, 1346, 238], [738, 772, 134], [924, 956, 172]]
    """


# yukarıda yazdığımız fonksiyonları test eden fonksiyon.
test()

""" 1.e)'de verdiğiniz cevabın karmaşıklığın farklı değerleri 
olabileceğini tartışınız, bunu nasıl mümkün olup olamayacağını belirtiniz.

cevap: beş adet matris çarpılması gerektiğinden en azından çarpılacak
ilk matrisin sütünü ve 2. matrisin satırı eşit olmalıdır.
eşit olması gerekmeyen satır ve sütunların sayısı 1 ise best case 
durumu olur ve karmaşıklık azalır. worst case'de ise matrislerin hepsinin
kare matris ve satır sütün sayılarının eşit olması gerekir. bu yüzden
karmaşıklık farklı değerler alabilir, bu mümkündür. """
