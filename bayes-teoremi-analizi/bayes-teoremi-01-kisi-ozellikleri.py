#!/usr/bin/python3
# created by cicek on May 09, 2020 06:38

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

'''
kaynak:
https://www.python-course.eu/naive_bayes_classifier_introduction.php
'''

# grafik için bakınız: ./figure_male-female.png

'''
./data.txt :
 boy, ağırlık, cinsiyet bilgilerinin bulunduğu rasgele 100 kişi içerir.

@class "feature" :
 sınıflandırma için kullanacak sınıf.

@params "male", "female" :
 Naive Bayes sınıflarıdan sadece 50 ölçüm değeri vardır.
 
@params "bin_width" :
 değerini 5 olarak ayarlamamız durumunda değerler
 "135 ila 139", "140 ila 144" ... aralıklarına bölünecektir.

@function "frekans" :
 belirli bir özellik değerinin hangi aralıkta tanımlı olduğunu ve
 bu aralıkta kaç tane benzer değer olduğunu döndüren fonksiyondur.
'''

genders = ["male", "female"]
persons = []

with open("data.txt") as fh:
    for line in fh:
        persons.append(line.strip().split())

firstnames = {}
heights = {}

for gender in genders:
    firstnames[gender] = [x[0] for x in persons if x[4] == gender]
    heights[gender] = [x[2] for x in persons if x[4] == gender]
    heights[gender] = np.array(heights[gender], np.int)

for gender in ("female", "male"):
    print(gender + ":")
    print(firstnames[gender][:10])
    print(heights[gender][:10])

'''
Veri kümesinin boy değerleri için iki özellik sınıfı oluşturuldu.
 Sınıflardan biri "male" sınıfının değerlerini
 diğeri ise "female" sınıfının değerlerini içerir.
'''


class Feature:

    def __init__(self, data, name=None, bin_width=None):
        self.name = name
        self.bin_width = bin_width

        if bin_width:

            # dosyadan minimum ve maksimum değerleri al.
            self.min, self.max = min(data), max(data)

            '''minimum değerden başlayıp maksimum değere kadar
               verilen artış miktarı(bin_width)ile bir liste oluştur'''
            bins = np.arange((self.min // bin_width) * bin_width,
                             (self.max // bin_width) * bin_width,
                             bin_width)
            print("bins ", bins)

            '''dosyadaki verilerin hangi aralıkta ve
               ne sıklıkta(freq) geçtiğini liste olarak oluştur.'''
            freq, bins = np.histogram(data, bins)
            # print("bins ",bins)
            # print("freq",freq)

            '''frekans değerlerini ve bu frekans değerlerine
               karşılık gelen aralıklardan bir dict oluştur.'''
            self.freq_dict = dict(zip(bins, freq))
            # print("freq dict",dict(zip(bins, freq)))
            # print("freq dict2", dict(Counter(data)))

            # frekans toplamını elde et.
            self.freq_sum = sum(freq)
            # print("freq_sum",sum(freq))
            # print("freq_sum2", sum(self.freq_dict.values()))

        else:
            '''herhangi bir aralık değeri verilmediği durumda frekans
               toplamını, yani üzerinde çalıştığımız verilerin
               boyutunu elde et.'''
            self.freq_dict = dict(Counter(data))

            '''herhangi bir aralık değeri verilmediği durumda
               veri içerisinde geçen her farklı değer için
               frekans değerini üret.'''
            self.freq_sum = sum(self.freq_dict.values())

    def frekans(self, value):
        if self.bin_width:
            # verilen değerin hangi aralığa denk geldiğini bul.
            value = (value // self.bin_width) * self.bin_width
            # print("value ",value)
        if value in self.freq_dict:
            '''verilen değerin bulunduğu aralıkta
               kaç tane daha değer olduğunu bul.'''
            # print("freq_dict3",self.freq_dict[value])
            return self.freq_dict[value]

        else:
            return 0


'''
@class "NBclass" :
 Bir NBclass 1 veya 1'den fazla Feature sınıfı içerir.
'''


class NBclass:

    def __init__(self, name, *features):
        self.features = features
        self.name = name

    def probability_value_given_feature(self, feature_value, feature):
        """
        p_value_given_feature returns the probability p
        for a feature_value 'value' of the feature to occurr
        corresponds to P(d_i | p_j)
        where d_i is a feature variable of the feature i
        """
        if feature.freq_sum == 0:
            return 0
        else:
            # değerin hangi olasılıkta ortaya çıktığını döndür.
            print("return1", feature.frekans(feature_value) / feature.freq_sum)
            return feature.frekans(feature_value) / feature.freq_sum


'''
Frekanslara göre listelere yaz ve bu değerlerin
 nasıl dağıldığını bir sütun grafiği ile görselleştir.
'''

fts = {}

for gender in genders:
    fts[gender] = Feature(heights[gender], name=gender, bin_width=5)
    print(gender, fts[gender].freq_dict)

for gender in genders:
    frequencies = list(fts[gender].freq_dict.items())
    frequencies.sort(key=lambda x: x[1])
    X, Y = zip(*frequencies)
    color = "blue" if gender == "male" else "red"
    bar_width = 4 if gender == "male" else 3
    plt.bar(X, Y, bar_width, color=color, alpha=0.75, label=gender)

plt.legend(loc='upper right')
plt.show()

'''
Uzunluk özelliği(heigts) ile NBclass sınıfı pluşturuldu.
 Daha önce oluşturulan ftrs özellik sınıflarını kullanıldı.
'''
cls = {}
for gender in genders:
    cls[gender] = NBclass(gender, fts[gender])

print("------------------------------------------>person\n\n")

'''
Basit bir Navie Bayes sınıfı oluşturmak için son adım 
 "NBclass" ve "Feature" sınıflarını kullanacak bir
 "Classifer" sınıfı yaratmak gerekir.
'''


class Classifier:

    def __init__(self, *nbclasses):
        self.nbclasses = nbclasses

    def prob(self, *d, best_only=True):
        print("------------------>prob")
        nbclasses = self.nbclasses
        probability_list = []
        for nbclass in nbclasses:
            ftrs = nbclass.features
            prob = 1

            '''Verilen değerin hangi sınıfta bulunabileceğinin
               olasılıksal olarak değerini yazdır'''
            for i in range(len(ftrs)):
                prob *= nbclass.probability_value_given_feature(d[i], ftrs[i])
                print("prob", prob)

            '''Olasılıkları hesaplanan değeri, bulunabileceği
               sınıf ve olasılık değeri ile listeye ekle'''
            probability_list.append((prob, nbclass.name))
            print("plist", probability_list)

        '''değişkenlerin olaslık değerlerini "prob_values"
           değişkenine liste olarak ata'''
        prob_values = [f[0] for f in probability_list]
        print("p_values", prob_values)

        '''değişkenlerin olasılık değerlerinin toplamını
           "prob_sum" değişkenine liste olarak ata'''
        prob_sum = sum(prob_values)
        print("p_sum", prob_sum)

        '''eğer sınıflandırmaya çalıştığımız değer
           sınıflar için eşit olasılkta ise'''
        if prob_sum == 0:
            number_classes = len(self.nbclasses)
            pl = []
            for prob_element in probability_list:
                pl.append(((1 / number_classes), prob_element[1]))
            probability_list = pl
            print("plist1", probability_list)

        # p_values değerlerini sırayla prob_sum değerlerine böl.
        else:
            probability_list = [(p[0] / prob_sum,
                                 p[1]) for p in probability_list]
            print("plist2", probability_list)
        if best_only:
            return max(probability_list)
        else:
            return probability_list


c = Classifier(cls["male"], cls["female"])

'''
Bir özellik olan uzunluk(heigts) değerine göre bir sınıflandırıcı
 oluşturuldu ve 130 ile 220 değerleri arasındaki değerler ile
 bu geğrlerin hangi cinsiyete ait bir değer olabileceğini kontrol et
'''

for i in range(130, 220, 5):
    print(i, c.prob(i, best_only=False))
print("------------------------------------------>for")

'''
Verilerde 140 ile 144 arasında bir boya sahip ne erkek ne de kadın
 olmadığından dolayı sınıflandırıcı, sonucu daha önceki verilere
 dayandıramaz ve bu nedenle %50 %50 olacak şekilde bir çıktı verir.
'''

'''
İsim özellikleri ile bir sınıflanrıcı eğitildi ve test
 isimlerindeki(testnames) isimlerin hangi cinsiyete ait olabileceği
 gösterildi.
'''

'''
"Jessie" isminin belirsiz bir isim olduğu görülür.
 Bu isimde 100 kişi için 66 kadın ismi olduğu görülmektedir.
'''
fts = {}
cls = {}
for gender in genders:
    fts_names = Feature(firstnames[gender], name=gender)
    cls[gender] = NBclass(gender, fts_names)

c = Classifier(cls["male"], cls["female"])

testnames = ['Edgar', 'Benjamin', 'Fred', 'Albert', 'Laura',
             'Maria', 'Paula', 'Sharon', 'Jessie']
for name in testnames:
    print(name, c.prob(name))

[person for person in persons if person[0] == "Jessie"]
print("------------------------------------------>person")

'''
Jessie Washington 159cm boyunda.
 Boy verisi ile eğitilmiş sınıflandırıcıya bakacak olursak
 159cm boyunda bir insanın "Kadın" olma olasılığının 0.875
 olduğunu görülür.

Peki ya "Jessie" adı verilen ve boyu bilinmeyen bir kişi için
 nasıl bir sonuç alnabilir? Bu kişi bir kadın mı yoksa erkek mi?
 Bu soruyu cevaplamak için iki farklı özellik ile eğitilmiş
 sınıflandırıcı kullanıldı ve çıktılar yazdırıldı.
'''

cls = {}
for gender in genders:
    fts_heights = Feature(heights[gender], name="heights", bin_width=5)
    fts_names = Feature(firstnames[gender], name="names")

    cls[gender] = NBclass(gender, fts_names, fts_heights)

c = Classifier(cls["male"], cls["female"])

for d in [("Maria", 140), ("Anthony", 200), ("Anthony", 153),
          ("Jessie", 188), ("Jessie", 159), ("Jessie", 160)]:
    print(d, c.prob(*d, best_only=False))

'''
output:

female:
['Stephanie', 'Cynthia', 'Katherine', 'Elizabeth', 'Carol', 'Christina', 'Beverly', 'Sharon', 'Denise', 'Rebbecca']
[149 174 183 138 145 161 179 162 148 196]
male:
['Randy', 'Jessie', 'David', 'Stephen', 'Jerry', 'Billy', 'Earl', 'Todd', 'Martin', 'Kenneth']
[184 175 187 192 204 180 184 174 177 200]
bins  [155 160 165 170 175 180 185 190 195 200 205]
male {155: 1, 160: 5, 165: 4, 170: 6, 175: 7, 180: 5, 185: 8, 190: 8, 195: 2, 200: 3}
bins  [130 135 140 145 150 155 160 165 170 175 180 185 190]
female {130: 1, 135: 1, 140: 0, 145: 3, 150: 5, 155: 7, 160: 8, 165: 11, 170: 7, 175: 2, 180: 4, 185: 0}
------------------------------------------>person


------------------>prob
return1 0.0
prob 0.0
plist [(0.0, 'male')]
return1 0.02040816326530612
prob 0.02040816326530612
plist [(0.0, 'male'), (0.02040816326530612, 'female')]
p_values [0.0, 0.02040816326530612]
p_sum 0.02040816326530612
plist2 [(0.0, 'male'), (1.0, 'female')]
130 [(0.0, 'male'), (1.0, 'female')]
------------------>prob
return1 0.0
prob 0.0
plist [(0.0, 'male')]
return1 0.02040816326530612
prob 0.02040816326530612
plist [(0.0, 'male'), (0.02040816326530612, 'female')]
p_values [0.0, 0.02040816326530612]
p_sum 0.02040816326530612
plist2 [(0.0, 'male'), (1.0, 'female')]
135 [(0.0, 'male'), (1.0, 'female')]
------------------>prob
return1 0.0
prob 0.0
plist [(0.0, 'male')]
return1 0.0
prob 0.0
plist [(0.0, 'male'), (0.0, 'female')]
p_values [0.0, 0.0]
p_sum 0.0
plist1 [(0.5, 'male'), (0.5, 'female')]
140 [(0.5, 'male'), (0.5, 'female')]
------------------>prob
return1 0.0
prob 0.0
plist [(0.0, 'male')]
return1 0.061224489795918366
prob 0.061224489795918366
plist [(0.0, 'male'), (0.061224489795918366, 'female')]
p_values [0.0, 0.061224489795918366]
p_sum 0.061224489795918366
plist2 [(0.0, 'male'), (1.0, 'female')]
145 [(0.0, 'male'), (1.0, 'female')]
------------------>prob

...
...
...

Process finished with exit code 0
'''
