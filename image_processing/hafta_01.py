#!/usr/bin/python3
# created by cicek on Oct 15, 2020 9:46 AM

import numpy as np
import matplotlib.pyplot as plt

list_1 = [1, 2, 3, 4, 5]

# görüntü 2 boyutlu bir veridir -> x, y
image_1 = plt.imread('pic_1.jpg')
# pixel, 400x600 resolution, dpi(dots per inch)

print(type(image_1))  # <class 'numpy.ndarray'> elemanlar aynı tip olmalı
print(image_1.shape)  # (480, 360, 3) -> (-y(satır), x(stun), her pixeldeki veri - rgb)
# PC'şer için sol üst orijin'dir.

print(image_1[0, 0, 0])  # 110
print(image_1[0, 0, 1])  # 136
print(image_1[0, 0, 2])  # 229

# for row in range(480):
#     for col in range(360):
#         # rgb, pixel, intensity (yoğunluk)
#         print(image_1[row, col, 0], image_1[row, col, 1], image_1[row, col, 2])
# ''' ...
# 140 132 129
# 161 153 150
# 98 90 87
# 33 25 22
# 8 0 0
# 15 7 4
# 34 26 23
# 8 0 0
# 11 3 0
# ... '''

"""

RGB(3 byte), -> .shape -> x,y,3
BW (1 bit), -> .shape -> x,y
gray level (1 byte), -> .shape -> x,y

color-map
digital image processing
computer vision
pinhole camera model
- intensity transformation -> tek pixele bakılıyorsa
- filter, morphology, spatial -> komşu pixellere bakılıyorsa
- frequency analysis
- mask
- OCR MNIST object
- NN CNN RNN DL
"""

# sudo pacman -S tk
plt.imshow(image_1)
plt.show()  # figure_1.png
