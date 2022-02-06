from passworddbclass import *

# ui part
print('''
şifre depolama sistemine hosgeldiniz

1- sifre oluşturma ve depolama

2- şifre ekle

3- ogren

cıkmak icin q ya basınız

''')

storage = Storage()

while True:

    islem = input("yapacagınız islem")

    if (islem == "q"):

        print("cikis yapılıyor...")
        break

    elif (islem == "1"):

        platformadi = input("platformadi:")
        kisa_adi = input("kısaltma")
        randomsifre = sifre_olustur()
        sifresi = randomsifre

        yeni_sifre = Password(platformadi, kisa_adi, sifresi)
        print("sifre ekleniyor")
        storage.sifre_ekle(yeni_sifre)
        print("sifre eklendi")




    elif (islem == "2"):

        platformadi = input("platformadi:")
        kisa_adi = input("kısaltma")
        sifresi = input("sifreniz:")

        yeni_sifre = Password(platformadi, kisa_adi, sifresi)
        print("sifre ekleniyor")
        storage.sifre_ekle(yeni_sifre)
        print("sifre eklendi")

    elif (islem == "3"):
        platform = input("platform adi:")
        storage.sifre_sorgu(platform)
    else:
        print("yanlış ya da hatalı işlem")
