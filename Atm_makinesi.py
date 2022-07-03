print("""******************************
Atm Makinesine Hoşgeldiniz.

İşlemler

1. Bakiye Sorgulama

2. Para Yatırma 

3. Para Çekme  

Programdan Çıkmak için 'q' ya basın.
*****************************************

""")

bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz:")

    if (işlem == "q"):
        print("Yine Bekleriz Efendim Bol Kazançlar Dilerim....")
        break

    elif (işlem == "1"):
        print("Bakiyeniz {} tl dir.".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Miktarı Giriniz:"))

        bakiye += miktar


    elif (işlem == "3"):
        miktar = int(input("Miktarı Griniz:"))

        if (bakiye - miktar < 0):
            print("Böyle Bir miktar çekemezsiniz")
            continue
        bakiye -= miktar


    else:
        print("Geçersiz İşlem....")









































