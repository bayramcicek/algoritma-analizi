#!/usr/bin/python3.6
# created by cicek on Mar 10, 2020 10:54


# empiric = deneme yanılma yaklaşımı


# list_1 = [0, 1, 2, 5]
# list_1[1] = -10
#
# print(list_1)  # [0, -10, 2, 5]
# list_1[10] = 45  # IndexError: list assignment index out of range

def check_prime(number):
    counter = 0

    if number != 1:
        for factor in range(2, number):
            counter = counter + 1

            if number % factor == 0:
                return False, counter
    else:
        return False, counter

    return True, counter


list = [10, 13, 23, 310, 311, 49]

for number in list:
    print("sayı:", number, check_prime(number))

# sayı: 10 (False, 1)
# sayı: 13 (True, 11)
# sayı: 23 (True, 21)
# sayı: 310 (False, 1)
# sayı: 311 (True, 309)
# sayı: 49 (False, 6)

# sayi 2'nin katı ise karmaşıklık -> O(1)
# tek ise yaklaşık -> O(n)
