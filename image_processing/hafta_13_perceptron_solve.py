#!/usr/bin/python3
# created by cicek on Dec 27, 2020 12:26 AM

from sklearn.datasets import fetch_openml
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

"""
SNN -> Single Layer Neural Network
LR -> logistic equation
-> sigmod

"""

epsilon = 1 * (10 ** (-5))


# sigmoid fonksiyonu
def sigmoid(z):
    s = 1 / (1 + np.exp(-z))
    return s


def compute_loss(Y, Y_hat):
    m = Y.shape[1]
    L = -(1. / m) * (np.sum(np.multiply(np.log(Y_hat + epsilon), Y)) + np.sum(
        np.multiply(np.log(1 - Y_hat + epsilon), (1 - Y))))

    return L


dataset = fetch_openml("mnist_784")  # 28x28

# print(type(dataset), type(dataset["data"]), type(dataset["target"]))
# # <class 'sklearn.utils.Bunch'> <class 'pandas.core.frame.DataFrame'> <class 'pandas.core.series.Series'>

X, y = dataset["data"], dataset["target"]

X = X / 255.0  # broadcasting normalize -> verileri 0 - 1 arasına getirdi.
# print(X.shape)  # (70000, 784) -> 7k resim var, 784 satır
# print(y.shape)  # (70000,)

""" X in 1.sütununu al. 1. sütunda 784 tane satır var.
Bunu 28x28 halinde 2D yapıya dönüştür. """
# i = 100
# img_1 = (X.values[i, :]).reshape(28, 28)
# # print(y[i])  # 0
#
# # resmi göster
# plt.imshow(img_1, cmap='gray')
# plt.title(y[i])
# plt.show()

# yeni
y_new = np.zeros(y.shape)
y_new[np.where(y == 0.0)[0]] = 1
y = y_new

m = 60000  # 7k dan 6k seçiyoruz eğitmek için.
m_test = X.shape[0] - m

# veriyi karıştır
X_train, X_test = X[:m].T, X[m:].T
y_train, y_test = y[:m].reshape(1, m), y[m:].reshape(1, m_test)

#
np.random.seed(138)
shuffle_index = np.random.permutation(m)
X_train, y_train = X_train.values[:, shuffle_index], y_train[:, shuffle_index]

#
learning_rate = 1

X = X_train
Y = y_train

n_x = X.shape[0]
m = X.shape[1]

W = np.random.randn(n_x, 1) * 0.01
b = np.zeros((1, 1))

for i in range(2000):
    Z = np.matmul(W.T, X) + b
    A = sigmoid(Z)

    cost = compute_loss(Y, A)

    dW = (1 / m) * np.matmul(X, (A - Y).T)
    db = (1 / m) * np.sum(A - Y, axis=1, keepdims=True)

    W = W - learning_rate * dW
    b = b - learning_rate * db

    if i % 100 == 0:
        print("Epoch", i, "cost: ", cost)

print("Final cost:", cost)
"""
Epoch 0 cost:  0.6780211644256914
Epoch 100 cost:  7.076902320959296e-06
Epoch 200 cost:  6.788042310395345e-06
Epoch 300 cost:  6.509536669410527e-06
Epoch 400 cost:  6.240823541302146e-06
Epoch 500 cost:  5.981381523350098e-06
Epoch 600 cost:  5.730726063487395e-06
Epoch 700 cost:  5.488406237169838e-06
Epoch 800 cost:  5.254001858304998e-06
Epoch 900 cost:  5.0271208844114535e-06
Epoch 1000 cost:  4.807397081508465e-06
Epoch 1100 cost:  4.59448791881352e-06
Epoch 1200 cost:  4.388072667200982e-06
Epoch 1300 cost:  4.1878506786998925e-06
Epoch 1400 cost:  3.993539827179672e-06
Epoch 1500 cost:  3.8048750928081097e-06
Epoch 1600 cost:  3.6216072750061147e-06
Epoch 1700 cost:  3.443501820447786e-06
Epoch 1800 cost:  3.2703377542419603e-06
Epoch 1900 cost:  3.101906703817453e-06
Final cost: 2.9396291168853755e-06

"""

#
Z = np.matmul(W.T, X_test) + b
A = sigmoid(Z)

predictions = (A.values > .5)[0, :]
labels = (y_test == 1)[0, :]

# doğruluk matrisi.  (0+1)/(9999-0) -> accuracy
"""
         T          F
T(1)   9999         1

F(1)    0           0

"""

"""
         T          F
T(1)     a          b

F(1)    c           d

    (c+b)       -> yanlış olan işlemler
    ------  -> accuracy
    (a+d)

Confusion matrix ile bir neural networkun performansı.

"""
print(confusion_matrix(predictions, labels))

print(classification_report(predictions, labels))
