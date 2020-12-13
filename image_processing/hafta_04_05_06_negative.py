#!/usr/bin/python3
# created by cicek on Nov 12, 2020 8:49 PM

# intensity information -> bir pixeldeki enerji seviyesi. (RGB)
# herhangi bir pixeli alıp oradaki renigine göre karar verip başka bir resim oluşturmak.

# bir fonksiyona sayısal değer atıyoruz bu fonk başka bi sayısal değer üretiyor.

import os
import matplotlib.pyplot as plt
import numpy as np


# bir intensity değerini başka bir intensity değerine çeviriyor.
# intensity arttırır
def my_f_1(a, b):
    assert a >= 0
    var = "intensity pozitive", "error intensity not positive"
    if a <= 255 - b:
        return a + b
    else:
        return 255


# intensity ile ->  resmin negatifini almış olduk
def my_f_2(a):
    # assert a >= 0
    # var = "intensity pozitive", "error intensity not positive"

    return int(255 - a)


def convert_rgb_to_gray_level(im_1):
    m = im_1.shape[0]
    n = im_1.shape[1]
    im_2 = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            im_2[i, j] = get_distance(im_1[i, j, :])
    return im_2


def get_distance(v, w=None):
    if w is None:
        w = [1 / 3, 1 / 3, 1 / 3]
    a, b, c = v[0], v[1], v[2]
    w1, w2, w3 = w[0], w[1], w[2]
    d = ((a ** 2) * w1 +
         (b ** 2) * w2 +
         (c ** 2) * w3) ** .5
    return d


print(os.getcwd(), os.listdir())
path = r"/home/cicek/PycharmProjects/image_processing/"
file_name_with_path = path + "cameraman.jpg"
img_0 = plt.imread(file_name_with_path)

print(file_name_with_path)  # /home/cicek/PycharmProjects/image_processingpic_sea.jpeg
print(img_0.ndim, img_0.shape)  # 3 (256, 256, 3)
print(np.min(img_0), np.max(img_0))  # 0, 255 (renkler aralığı)

img_1 = convert_rgb_to_gray_level(img_0)
print(img_1.ndim, img_1.shape)  # 2 (256, 256)

m, n = img_1.shape
img_2 = np.zeros((m, n), dtype="uint8")

for i in range(m):
    for j in range(n):
        # intensity = img_1[i, j]
        # increment = 50
        # img_2[i, j] = my_f_1(intensity, increment)
        intensity = img_1[i, j]
        img_2[i, j] = my_f_2(intensity)

print(np.min(img_1), np.max(img_1))  # 0.0 255.0
print(np.min(img_2), np.max(img_2))  # 50 255

print(my_f_2(243))  # 12

plt.subplot(1, 2, 1)
plt.imshow(img_1, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(img_2, cmap='gray')
plt.show()
