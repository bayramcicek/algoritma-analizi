import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


#Aşağıdaki listelerden "in_time" Hamburg treni aktarma trani olan Münih trenini yakalamak için zamanaında gelmesini
#"too_late" ise aktarma trenin kaçırılmış olduğu durumları gösteren birkaç haftayı kapsayan verilerdir.Her listenin
#içindeki elemanları ilk bileşeni trenin kaç dakika geç kaldığını ikinci bileşen ise bunun gerçekleşme süresini ifade eder.

#
# the tuples consist of (delay time of train1, number of times)
# tuples are (minutes, number of times)

in_time = [(0, 22), (1, 19), (2, 17), (3, 18),
           (4, 16), (5, 15), (6, 9), (7, 7),
           (8, 4), (9, 3), (10, 3), (11, 2)]
too_late = [(6, 6), (7, 9), (8, 12), (9, 17),
            (10, 18), (11, 15), (12,16), (13, 7),
            (14, 8), (15, 5)]

X, Y = zip(*in_time)

X2, Y2 = zip(*too_late)

bar_width = 0.9
plt.bar(X, Y, bar_width,  color="blue", alpha=0.75, label="in time")
bar_width = 0.8
plt.bar(X2, Y2, bar_width,  color="red", alpha=0.75, label="too late")
plt.legend(loc='upper right')
plt.show()

# Bu verilere bakarak, 1 dakika geç kalmamız durumunda, aktarma trenini yakalama olasılığımızın 1 olduğunu söyleyebiliriz çünkü
# 19 başarılı durum gerçekleşmiş ve tren hiç kaçırılmamış yani "too_late" içindeki elemanlardan ilk bileşeni 1 olan veri yok.

in_time_dict = dict(in_time)
too_late_dict = dict(too_late)

def catch_the_train(min):
    s = in_time_dict.get(min, 0)
    if s == 0:
        return 0
    else:
        m = too_late_dict.get(min, 0)
        return s / (s + m)

for minutes in range(-1, 13):
    print(minutes, catch_the_train(minutes))

print("----------------------------------------------------------------------------------------")

# -------------------------------------------------------------------------------------------------------------------------

# data.txt adlı dosya  boy, ağırlık, ve cinsiyet bilgilerinin bulunduğu rasgele 100 kişi içermektedir.

# Sınıflandırma için kullanacağımız "feature" isimli bir sınıf tanımladık. Özellik değerlerinin sayısal olduğu
# durumlarda, olası özellik değerlerini azaltmak için bunları bölmek isteyebiliriz. Kişilerin  boyları geni bir
# aralığa sahiptir ve Naive Bayes sınıflarımızdan "male" ve "female" için sadece 50 ölçüm değerine sahibiz.
# bin_width değerini 5 olarak ayarlamamız durumunda değerleri "130 ila 134", "135 ila 139", "140 ila 144" aralıklarına
# bölmüş olacağız. frekans metodu belirli bir özellik değerinin hangi tanımlı aralıkta olduğunu ve bu aralıkta kaç tane
# benzer değer olduğunu döndüren metottur.

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

# -------------------------------------------------------------------------------------------------------------------------
# Veri kümesinin boy değerleri için iki özellik sınıfı oluşturduk. Sınıflardan biri "male" sınıfının
# değerlerini diğeri ise "female" sınıfının değerlerini içerir.
class Feature:

    def __init__(self, data, name=None, bin_width=None):
        self.name = name
        self.bin_width = bin_width
        if bin_width:
            # Verideki(data) minimum ve maksimum değerleri elde ettik.
            self.min, self.max = min(data), max(data)

            # minimum değerden başlayıp maksimum değere kadar  verilen artış miktarı(bin_width) ile bir liste oluşturduk.
            bins = np.arange((self.min // bin_width) * bin_width,
                             (self.max // bin_width) * bin_width,
                             bin_width)
            print("bins ",bins)

            # Verideki(data) verilerin hangi aralıkta ve ne sıklıkta(freq) geçtiğiniliste olarak elde ettik.
            freq, bins = np.histogram(data, bins)
            # print("bins ",bins)
            # print("freq",freq)

            # frekans değerlerini ve frekans değerlerine karşılık gelen aralıklardan bir dict elde ettik.
            self.freq_dict = dict(zip(bins, freq))
            # print("freq dict",dict(zip(bins, freq)))
            # print("freq dict2", dict(Counter(data)))
            # frekans toplamını, yani üzerinde çalıştığımız veri stenin boyutunu elde ettik.
            self.freq_sum = sum(freq)
            # print("freq_sum",sum(freq))
            # print("freq_sum2", sum(self.freq_dict.values()))
        else:
            # herhangi bir aralık değeri verilmediği durumda
            # frekans toplamını, yani üzerinde çalıştığımız veri stenin boyutunu elde ettik.
            self.freq_dict = dict(Counter(data))
            # herhangi bir aralık değeri verilmediği durumda
            # veri içerisinde geçen her farklı değer için frekans değerini elde ettik
            self.freq_sum = sum(self.freq_dict.values())

    def frekans(self, value):
        if self.bin_width:
            # verilen değerin hangi aralığa denk geldiğini elde ettik.
            value = (value // self.bin_width) * self.bin_width
            # print("value ",value)
        if value in self.freq_dict:
            # verilen değerin bulunduğu aralıkta kaç tane daha değer olduğunu elde ettik.
            # print("freq_dict3",self.freq_dict[value])
            return self.freq_dict[value]

        else:
            return 0

# -------------------------------------------------------------------------------------------------------------------------
# Bir naive bayes sınıfı (NBsinifi) tasarladık. Bir NBsinifi bir veya birden daha fazla Ozellik  sınıfı içerir.
# NBs bir veya birden fazla Feature sınıfı içerir. NBclass adı self.name içinde saklanır.
class NBclass:

    def __init__(self, name, *features):
        self.features = features
        self.name = name

    def probability_value_given_feature(self,feature_value,feature):
        """
        p_value_given_feature returns the probability p
        for a feature_value 'value' of the feature  to occurr
        corresponds to P(d_i | p_j)
        where d_i is a feature variable of the feature i
        """

        if feature.freq_sum == 0:
            return 0
        else:
            # değerin hangi olasılıkta ortaya çıkıtğını döndürdük.
            # print("return1",feature.frekans(feature_value) / feature.freq_sum)
            return feature.frekans(feature_value) / feature.freq_sum

# -------------------------------------------------------------------------------------------------------------------------
# Listelere frekanslara göre sınıfları yazdırdık ve bu değerlerin nasıl dağıldığını bir sütun grafiği ile görselleştirdik.
fts = {}
for gender in genders:
    fts[gender] = Feature(heights[gender], name=gender, bin_width=5)
    print(gender, fts[gender].freq_dict)

for gender in genders:
    frequencies = list(fts[gender].freq_dict.items())
    frequencies.sort(key=lambda x: x[1])
    X, Y = zip(*frequencies)
    color = "blue" if gender=="male" else "red"
    bar_width = 4 if gender=="male" else 3
    plt.bar(X, Y, bar_width, color=color, alpha=0.75, label=gender)

plt.legend(loc='upper right')
plt.show()
print("----------------------------------------------------------------------------------------")

# -------------------------------------------------------------------------------------------------------------------------
# Alttaki kod ile, bir özellik yani uzunluk özelliği(heigts) ile NBclass sınıfı oluşturduk. Daha önce
# oluşturduğumuz fts özellik sınıflarını kullandık.
cls = {}
for gender in genders:
    cls[gender] = NBclass(gender, fts[gender])
print("----------------------------------------------------------------------------------------")

# -------------------------------------------------------------------------------------------------------------------------
# Basit bir Navie Bayes sınıfı oluşturmak için son adım "NBclass" ve "Feature" sınıflarımızı kullanacak bir
# "Classifer sınıfı yazmamız gerekmektedir.
class Classifier:

    def __init__(self, *nbclasses):
        self.nbclasses = nbclasses

    def prob(self, *d, best_only=True):
        print("------------------")
        nbclasses = self.nbclasses
        probability_list = []
        for nbclass in nbclasses:
            ftrs = nbclass.features
            prob = 1

            # "Verilen değerin hangi sınıfta  bulunabileceğinin olaslıklasal olarak değerini yazdırdık"
            for i in range(len(ftrs)):
                prob *= nbclass.probability_value_given_feature(d[i], ftrs[i])
                print("prob",prob)

            # Olasılıklarını hesapladığımız değeri bulunabileceği sınıf ve olaslık değeri ile listeye ekledik.
            probability_list.append((prob, nbclass.name))
            print("plist", probability_list)

        # değişkenlerin olaslık değerlerini  "prob_values" değişkenine liste olarak atadık.
        prob_values = [f[0] for f in probability_list]
        print("p_values",prob_values)

        # değişkenlerin olaslık değerlerinin toplamını  "prob_sum" değişkenine liste olarak atadık.
        prob_sum = sum(prob_values)
        print("p_sum",prob_sum)

        # Eğer sınıflandırmaya çalıştığımız değeri sınfılar için eşit olasılkta ise
        if prob_sum == 0:
            number_classes = len(self.nbclasses)
            pl = []
            for prob_element in probability_list:
                pl.append(((1 / number_classes), prob_element[1]))
            probability_list = pl
            print("plist1",probability_list)

        # p_values değerlerini sırayla prob_sum değerlerine böldük
        else:
            probability_list = [(p[0] / prob_sum, p[1]) for p in probability_list]
            print("plist2", probability_list)
        if best_only:
            return max(probability_list)
        else:
            return probability_list

c = Classifier(cls["male"], cls["female"])

print("----------------------------------------------------------------------------------------")
# -------------------------------------------------------------------------------------------------------------------------
# Bir özellik olan uzunluk(heigts) değerine göre  bir sınıflandırıc oluşturduk ve 130 ile 220 değerleri arasındaki
# değerlerle hangi cinsiyete ait bir değer olabileceğini kontrol ettik.

for i in range(130, 220, 5):
    print(i, c.prob(i, best_only=False))
print("----------------------------------------------------------------------------------------")

# Eğitim veristemizde 140 ile 144 arasında bir boya sahip ne erkek ne de kadin olmadığından dolayı sınıflandırıcımız sonucu
# daha önceki verilere dayandıramaz ve bu nedenle yüzde 50 yüzde 50 olucak şekilde bir çıktı verir.


# -------------------------------------------------------------------------------------------------------------------------
# İsim özellikleri ile bir sınıflanrıcı eğittik ve test isimlerindeki(testnames) isimlerin hangi cinsiyete ait olabileceğini
# gösterdik.

# "Jessie" isminin belirsiz bir isim olduğunu görüyoruz. Bu isimde 100 kişi için 66 kadın ismi olduğu görülmektedir.
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
print("----------------------------------------------------------------------------------------")

# -------------------------------------------------------------------------------------------------------------------------
# "Jessie Washington 159cm boyunda. Boy verisi ile eğitilmiş sınıflandırıcımıza bakacak olursak 159 cm boyunda bir insanın "Kadin"
# olma olasılığının 0.875 olduğunu görebiliriz. Peki ya "Jessie" adı verilen ve boyu bilinmeyen bir kişi için nasıl bir sonuç alırız?
# Bu kiş bir kadın mıdır yoksa erkek mi? Bu soruyu cevaplamak için iki farklı özellik ile eğitilmiş sınıflandırıcısını kullandık ve
# çıktıları yazdırdık.

cls = {}
for gender in genders:
    fts_heights = Feature(heights[gender], name="heights", bin_width=5)
    fts_names = Feature(firstnames[gender], name="names")

    cls[gender] = NBclass(gender, fts_names, fts_heights)


c = Classifier(cls["male"], cls["female"])

for d in [("Maria", 140), ("Anthony", 200), ("Anthony", 153),
          ("Jessie", 188) , ("Jessie", 159), ("Jessie", 160) ]:
    print(d, c.prob(*d, best_only=False))
print("----------------------------------------------------------------------------------------")