#!/usr/bin/python3
# created by cicek on May 08, 2020 15:46

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

'''
kaynak:
https://www.python-course.eu/naive_bayes_classifier_introduction.php
'''

# grafik için bakınız: ./figure_in-time-too-late.png

'''
@list "in_time" :
 Hamburg treninin, aktarma treni olan Münih trenini yakalamak için
 zamanında gelmesini temsil eder.
 
@list "too_late" :
 aktarma trenin kaçırılmış olduğu durumları gösteren
 birkaç haftayı kapsayan verilerdir.
 
Her listenin içindeki ikili elemanların
 1.ci bileşeni: trenin kaç dakika geç kaldığını gösterir.
 2.ci bileşeni: bunun gerçekleşme süresini ifade eder.
'''

# the tuples consist of (delay time of train1, number of times)
# tuples are (minutes, number of times)

in_time = [(0, 22), (1, 19), (2, 17), (3, 18),
           (4, 16), (5, 15), (6, 9), (7, 7),
           (8, 4), (9, 3), (10, 3), (11, 2)]

too_late = [(6, 6), (7, 9), (8, 12), (9, 17),
            (10, 18), (11, 15), (12, 16), (13, 7),
            (14, 8), (15, 5)]

X, Y = zip(*in_time)
X2, Y2 = zip(*too_late)

bar_width = 0.9
plt.bar(X, Y, bar_width, color="blue", alpha=0.75, label="in time")

bar_width = 0.8
plt.bar(X2, Y2, bar_width, color="red", alpha=0.75, label="too late")

plt.legend(loc='upper right')
plt.show()

'''
Grafik için bakınız: ./figure_in-time-too-late.png

Bu verilere bakarak, Hamburg treninin 5 ve daha az dakika geç kalması
 durumunda, aktarma trenini yakalama olasılığı 1'dir.

12. dakikadan sonra ise aktarma trenine yetişme olasılığı 0'a düşer.
    
Yani burada koşullu olasılık vardır. Bayes teoremi'ne göre aktarma
 trenine yetişebilme ihtimalini ölçebilmemiz için önce Hamburg treninin
 kaç dakika geç kaldığını bilmemiz gerekir.
'''

in_time_dict = dict(in_time)
too_late_dict = dict(too_late)

# counter = 0
'''
counter değişkeni sadece 1 defa çalışır.
 bu yüzden karmaşıklık -> O(1)
'''
def catch_the_train(min):
    s = in_time_dict.get(min, 0)
    # global counter
    if s == 0:
        return 0
    else:
        # counter += 1
        m = too_late_dict.get(min, 0)
        # print("counter -> ", counter)
        return s / (s + m)


# karmaşıklık -> O(1)
for minutes in range(0, 13):
    print(minutes, catch_the_train(minutes))

'''
output:

0 1.0
1 1.0
2 1.0
3 1.0
4 1.0
5 1.0
6 0.6
7 0.4375
8 0.25
9 0.15
10 0.14285714285714285
11 0.11764705882352941
12 0

Process finished with exit code 0
'''
