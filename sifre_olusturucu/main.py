import random

karakterler = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre_uzunlugu = int(input("Şifrenin uzunluğu ne kadar olsun?\n"))

sifre = ""

for i in range(sifre_uzunlugu):
    sifre += random.choice(karakterler)

print(sifre)