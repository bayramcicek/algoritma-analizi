#!/usr/bin/python3
# created by cicek on Jan 08, 2021 2:04 PM

from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import numpy as np

dataset = fetch_openml("mnist_784")

print(type(dataset), type(dataset["data"]), type(dataset["target"]))

X, y = dataset["data"], dataset["target"]

X = X / 255.0  # broadcasting normalize -> verileri 0 - 1 arasına getirdi.
print(X.shape, y.shape)

i = 10010
img_1 = (X.values[i, :]).reshape(28, 28)
print(y[i])  # 0

# resmi göster
plt.imshow(img_1, cmap='gray')
plt.title(y[i])
plt.show()

digits = 10
examples = y.shape[1]

y = y.reshape(1, examples)

Y_new = (np.eye(digits))[y.astype('int32')]
Y_new = Y_new.T.reshape(digits, examples)
