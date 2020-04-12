#!/usr/bin/python3.6
# created by cicek on Apr 12, 2020 12:33

# C'deki temel veri yapılarını destekleyen bir kütüphane
import ctypes  # provides low-level arrays
import sys
from pympler import asizeof

'''
https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275

Ağaçlar, listeler, graph/hash yapıları -> Abstract Data Types
herkes bunları kendi isteğine göre modelleyebilir

list -> array veya pointer temelli
binary search tree -> pointer ile oluşturulabilir fakat array ile de yapılabilir

Yani bir ABS'nin iç yapısı son kullanıcıya kapalıdır(internal)
    internal yapı 2 farklı şekilde olabilir:
        - array ile oluşturulan
        - pointer ile oluşturulan

- list arama maliyeti O(n) veya O(logn) gibi değişebilir.
- Amortized cost için array yapısı olması gerekiyor.

- Bütün veri yapılarının teml fonksiyonları tanımlanmıştır
    fakat iç yapısı tanımlı değildir. iç yapı tamammen geliştiricinin tercihidir.

- Array varsa mutlaka amortized karmaşıklıktan bahsetmek gerekiyor.
    örneğin insert için sırasıyla karmaşıklık 1, 1, 1, ... oldu fakat
    liste doldu ve bir yerde karmaşıklık n oldu. n tane işlemin karmaşıklığı
    için n tane 1 var + 1 tane n var toplayıp n'e bölersek yaklaşık 2 çıkıyor.
    bu değeri 1 olarak yazıyoruz ve bu amortized cost'ta, sistemin n operasyonda
    bir defa worst case'e gireceğini gösterir.

- Python'daki bazı kütüphaneler C ile yazılmıştır daha hızlı olması için.
- Python'da classlarda, içerde o sınıfa ait bir değişken kullanılacaksa mutlaka
    self kullanılmalıdır.

'''


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def getsize(self):
        import sys
        try:
            # _A array'i gösterir. bellekte kapladığı yeri geri gönder.
            return sys.getsizeof(self._A)

        except:
            return 0

    def ToString(self):
        try:
            for i in self._A:
                print(i, " ")
        except:
            pass

    def getLength(self):
        return len(self._A)

    def __init__(self):
        """Create an empty array."""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity

        # 1 elemanlı bir yapı oluştur.
        self._A = self._make_array(self._capacity)  # low-level array

    def _make_array(self, c):  # nonpublic utitity
        """Return new array with capacity c."""

        # C'deki malloc() gibi
        return (c * ctypes.py_object)()  # see ctypes documentation

    def append(self, obj):
        """Add object to end of the array."""
        # n -> kaç tane eleman var.
        # _capacity -> toplam boyut
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)  # new (bigger) array
        print(" şu an amortized cost işlemi ... ")
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
            print(" şu an move işlemi ... ")

        # B'nin pointer'ını A'nın pointer'ının üzerine yaz
        self._A = B  # use the bigger array
        self._capacity = c

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def len_n(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]  # retrieve from array

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        for j in range(self._n, k, -1):  # shift rightmost first
            self._A[j] = self._A[j - 1]
        self._A[k] = value  # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:  # found a match!
                for j in range(k, self._n - 1):  # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None  # help garbage collection
                self._n -= 1  # we have one less item
        return  # exit immediately
        raise ValueError('value not found')  # only reached if no match


c = DynamicArray()
print(c.getLength(), c.getsize(), c.len_n())  # 1 136 0

c = DynamicArray()
for i in range(6):
    c.append(-100)
print(c.getLength(), c.getsize(), c.len_n())  # 8 136 6

'''
out:

1 136 0
 şu an amortized cost işlemi ... 
 şu an move işlemi ... 
 şu an amortized cost işlemi ... 
 şu an move işlemi ... 
 şu an move işlemi ... 
 şu an amortized cost işlemi ... 
 şu an move işlemi ... 
 şu an move işlemi ... 
 şu an move işlemi ... 
 şu an move işlemi ... 
8 136 6
'''

# s_1 = sys.getsizeof(c)
# s_2 = asizeof.asizeof(c)
#
# print("s_1 : {0}, s_2 : {1}".format(s_1, s_2))
# '''
# out:
# s_1 : 56, s_2 : 648
#
# - 56 birimlik yer var.
# - fakat gerçekte 648(byte) birimlik yer işgal ediyor
#
# '''

# def ata():
#     n = 10
#     for i in range(n):
#         c.append(12)
#         c.append("sdfsdfsdf")
#
#     s_1 = sys.getsizeof(c)
#     s_2 = asizeof.asizeof(c)
#     print("n s_1 : {0}, s_2 : {1}".format(s_1, s_2))
#
#
# ata()
# print(c.getLength(), c.getsize())  # 32 136
# '''
# out:
#
# s_1 : 56, s_2 : 648
#  şu an amortized cost işlemi ...
#  şu an move işlemi ...
#  şu an amortized cost işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an amortized cost işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an amortized cost işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an amortized cost işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
#  şu an move işlemi ...
# n s_1 : 56, s_2 : 656
# 32 136
#
# Process finished with exit code 0
#
# '''

# for i in range(1800):
#     c.append(i)
#     # c.ToString()
# print("len : {0}".format(c.getLength()),end=" ")
# print("size : {0}".format(c.getsize()))
# print("len_n : {0}".format(c.len_n()))
#
# '''
# out:
#
# len : 2048 size : 136
# len_n : 1800
# '''
