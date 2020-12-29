#!/usr/bin/python3
# created by cicek on Dec 27, 2020 12:26 AM

import numpy as np

"""
MLP - Multilayer perceptron (1den fazla perceptron)
CNN - Convolutional neural network(deeplearning 'te en fazla kul. mimari)
    -> tek bir veriyi alır 

RNN -> Recurrent neural network

perceptron -> MLP -> CNN

input -> işleme -> output
input bilgisini alıp işleyip dışarıya output vermek: perceptron

[x^t x y] -> dot product üretir.

xn wn -> çarpımlar toplanır. Activation function > 0 ise true, değilse false.
Bu model XOR gibi ilnearly separable olmayan veriler için doğru sonucu vermez. 

Perceptron Learning Algorithm -> PLA
    -> error 0 olana kadar iterasyon

inputları belli bir ağırlık ile karşılıklı çarpıp 0 dan + veya - bakıp 0, 1 veya true, false kararını veriyor. 
"""


class Perceptron(object):
    """implements a perception network"""

    # constructor: veri boyutunu alarak W ağırlığını oluşturur.
    def __init__(self, input_size, lr=1, epochs=10):  # kaç tane veri girecek ise onun boyutu
        self.W = np.zeros(input_size + 1)
        # add one for bias
        self.epochs = epochs
        self.lr = lr

    # x ve W nin dot çarpımından gelen sayının 0 'dan büyük/küçük olması durumunda 0/1 gönderir.
    def activation_fn(self, x):
        return 1 if x >= 0 else 0

    # W nin transpozeini alıp dot olarak çarpıp tek değer üretir. Bu değeri activation_fn üzerinden 0 veya 1 döner.
    def predict(self, x):
        x = np.insert(x, 0, 1)
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a

    # verileri oluştur ve error değerine göre güncelle
    def fit(self, X, d):  # d -> kaç tane veri var
        for _ in range(self.epochs):
            for i in range(d.shape[0]):  # kaç tane veri verilmişse
                y = self.predict(X[i])
                e = d[i] - y
                self.W = self.W + self.lr * e * np.insert(X[i], 1, 0)


# # # # bir resim olsun ve 100x100 ise input size:
# # # mp = Perceptron(100 * 100)
# # mp = Perceptron(5)
# # print(mp.W)  # out: [0. 0. 0. 0. 0. 0.] -> x^t + b
# # print(mp.activation_fn(10))  # 1
# # print(mp.activation_fn(-10))  # 0
#
# mp = Perceptron(5)
# x = np.asarray([1, 2, 3, 4, 5])  # ndarray dim different
# res = mp.predict(x)
# print(res)  # 1

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

d = np.array([0, 0, 0, 1])  # AND
perceptron = Perceptron(input_size=2)
print(perceptron.W)  # [0. 0. 0.]
perceptron.fit(X, d)
print(perceptron.W)  # [-3.  2.  1.] şeklinde bir model oluştu

# d = np.array([0, 1, 1, 0])  # XOR
# perceptron = Perceptron(input_size=2)
# print(perceptron.W)  # [0. 0. 0.]
# perceptron.fit(X, d)
# print(perceptron.W)  # [-1.  0. -1.] şeklinde bir model oluştu

"""
-- ÖDEV --

1. Perceptron class tanımınında var olan fonksiyonları kısaca tanıtınız.

    def __init__(self, input_size, lr=1, epochs=10) -> constructor: veri boyutunu alarak W ağırlığını oluşturur.
    def activation_fn(self, x) -> x ve W nin dot çarpımından gelen sayının 0 'dan büyük/küçük olması durumunda 0/1 gönderir.
    def predict(self, x) ->  W nin transpozeini alıp dot olarak çarpıp tek değer üretir. Bu değeri activation_fn üzerinden 0 veya 1 döner.
    def fit(self, X, d) -> verileri oluştur ve error değerine göre güncelle
    
2. XOR için verileri değiştirip çalışmasını gözlemleyiniz.
    
    d = np.array([0, 1, 1, 0])  # XOR
    perceptron = Perceptron(input_size=2)
    print(perceptron.W)  # [0. 0. 0.]
    perceptron.fit(X, d)
    print(perceptron.W)  # [-1.  0. -1.] şeklinde bir model oluştu

3. Bu class ile dersimize kayıtlı 40 öğrenci için imza tanıması yapılırsa
   X ve d değerlerini ne olur, predict fonksiyonu nasıl kullanılır açıklayınız
    imza verileri siyah/beyaz duruma çevrilirse dizi:
    [[1 1 1 ... 1 1 1]
     [0 1 1 ... 1 1 1]
     [1 1 1 ... 1 1 1]
     ...
     [0 0 0 ... 0 0 0]
     [0 0 0 ... 0 0 0]
     [0 0 0 ... 0 0 0]]
     
     Öyleyse; (her resim verisi için)
     X = np.array([
        [1 1 1 ... 1 1 1]
        [0 1 1 ... 1 1 1]
        [1 1 1 ... 1 1 1]
        ...
        [0 0 0 ... 0 0 0]
        [0 0 0 ... 0 0 0]
        [0 0 0 ... 0 0 0]
    ])
    
    d = np.array([0, 0, 0, 1])  # AND
    
    predict(self, x) fonksiyonunda verilerin dot çarpımı yapılıp activation
     fonksiyonuna yollayıp her imza için farklı bi değer bulunur.
    
    Her 40 imza verisi için farklı modeller oluşturulur.
    
4. Bu modelin hatası nasıl elde edilir, kendi çözümünüzü/yorumunuzu yazınız.

    Her xn ve wn çarpımları alınıp toplandığında ve activation
      fonksiyondan > 0 ise true, değilse false döner fakat
      bu model XOR gibi linearly separable olmayan veriler
      için doğru sonucu vermez.

"""
