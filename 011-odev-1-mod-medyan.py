#!/usr/bin/python3.6
# created by cicek on Apr 04, 2020 20:14

import random

'''
- ödev 1 mode medyan karmaşıklığı
Due April 05 at 11:59 PM
Instructions: mode ve medyanın her ikisini return edecek şekilde bir fonksiyon yazınız. Fonksiyon içerisinden 
              başka bir fonksiyona çağrım yapılmayacaktır.

import random
def getModeMedian(list_1):

    ....
   # bubble, histogram vs. için ek çağrım yapılmadan bütün işlemler burada yapılmalıdır.
   # küçük bloklar halinde yazdığınız fonksiyonun karmaşıklığını # ile comment olarak açıklayınız
   ...

   return mode,median
'''


# O(n^2) + O(1) + O(n) + O(n) -> (n^2 + 2n + 1) olduğundan
# get_mode_median(list) ortalama karmaşıklık (average case) -> O(n^2) olması gerek.
def get_mode_median(list):
    uzunluk = len(list)
    mode = -1
    median = -1

    # listeyi sırala (insertion sort) -> O(n^2)
    # for karmaşıklık -> n
    for i in range(1, uzunluk):
        key = list[i]
        j = i - 1

        # while - karmaşıklık -> n
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = key

    # # sıralanmış liste
    # print(list)

    # ortanca(median) - karmaşıklık -> O(1)
    if uzunluk % 2 == 0:
        # print((list[int((uzunluk / 2) - 1)] + list[int(uzunluk / 2)]) / 2)
        median = ((list[int((uzunluk / 2) - 1)] + list[int(uzunluk / 2)]) / 2)
    else:
        # print(list[int(((uzunluk + 1) / 2) - 1)])
        median = (list[int(((uzunluk + 1) / 2) - 1)])

    # tüm elemanların tekrarını tutacak dictionary
    tepe_dict = {}
    global counter
    counter = 1

    # her elemanın tekrarını bul -  karmaşıklık -> O(n)
    for i in range(uzunluk - 1):

        if (list[i] == list[i + 1]):
            counter += 1
            if ((i + 2) == uzunluk):
                tepe_dict[list[i]] = counter
                counter = 1
        else:
            tepe_dict[list[i]] = counter
            counter = 1
            if ((i + 2) == uzunluk):
                counter = 1
                tepe_dict[list[i + 1]] = counter

    # # tekrarlı elemanları içeren dict
    # print(tepe_dict)

    global tepe_key, tepe_value
    tepe_key, tepe_value = -1, -1

    '''
    tepe değeri bul. eğer tepe değer 1'den fazla ise kolaylık açısından
    ortalamasını al - karmaşıklık -> O(n)
    '''
    for key, value in tepe_dict.items():
        if (value > tepe_value):
            tepe_key, tepe_value = key, value
        elif (value == tepe_value):
            tepe_key, tepe_value = ((tepe_key + key) / 2), value

    # print(tepe_key, tepe_value)

    mode = tepe_key
    return mode, median


# listeyi rastgele ata
list = []
for i in range(5000):
    list.append(random.randint(0, 100))

# çıktıyı al
result = get_mode_median(list)
print(result)  # (mode, median)
