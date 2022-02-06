import sqlite3
import random


def sifre_olustur():
    numberlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lowercase_letterlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase_letterlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    specialcharlist = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '}',
                       '{', '|', ';', "'", ':', '"', ',', '.', '/', '<', '>', '?']

    print("sorulara 'Y' be 'N' olarak cevap verin")
    numbercheck = input("rakam olsun mu")
    lowercasecheck = input("küçük harf olsun mu")
    uppercasecheck = input("büyük harf olsun mu")
    specialcheck = input("özel karakterler olsun mu")
    final_list = []

    if numbercheck == "Y":
        final_list += numberlist

    if lowercasecheck == "Y":
        final_list += lowercase_letterlist

    if uppercasecheck == "Y":
        final_list += uppercase_letterlist

    if specialcheck == "Y":
        final_list += specialcharlist

    else:
        pass

    lenghtpass = int(input("sifrenin uzunlugu ne kadar olsun"))
    print(final_list)
    final_list_last = []

    for i in range(0, lenghtpass):
        index = random.randint(0, len(final_list))
        final_list_last.append(final_list[index])
    print(final_list_last)
    final_password = "".join(final_list_last)
    print("son sifreniz: {}".format(final_password))

    return final_password


class Password():
    def __init__(self, platform, kisa_ad, sifre):
        self.platform = platform
        self.kisa_ad = kisa_ad
        self.sifre = sifre

    def __str__(self):
        return "platform adi:{}\nkisaltma:{}\nsifre:{}".format(self.platform, self.kisa_ad, self.sifre)


class Storage():

    def __init__(self):
        self.baglanti_kur()

    def baglanti_kur(self):
        self.baglanti = sqlite3.connect("storage.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS sifreler(platform TEXT,kisatma TEXT,sifre TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def sifre_ekle(self, sifre):
        sorgu = "INSERT INTO sifreler VALUES(?,?,?)"

        self.cursor.execute(sorgu, (sifre.platform, sifre.kisa_ad, sifre.sifre))

        self.baglanti.commit()

    def sifre_sorgu(self, platform):
        sorgu = "Select * From sifreler where platform=?"
        self.cursor.execute(sorgu, (platform,))
        sifreler = self.cursor.fetchall()
        if (len(sifreler) == 0):
            print("böyle bir sifre yok")
        else:
            sifre_sorguda = Password(sifreler[0][0], sifreler[0][1], sifreler[0][2], )
            print(sifre_sorguda)
