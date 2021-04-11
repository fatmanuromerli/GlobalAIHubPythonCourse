import time

print("***********************************************\n"
      "BİLGİ YARIŞMAMIZA HOŞGELDİNİZ\n"
      "***********************************************\n")

time.sleep(2)
ad = input("adınızı giriniz : ")
soyad = input("soyadınızı giriniz : ")

print(f"Merhaba {ad} {soyad}. Yarışmamıza hoşgeldiniz. Yarışma kurallarımız aşağıdaki gibidir. \n\n")
time.sleep(2)

print(" 10 soru 10 cevap şeklinde olacaktır.\n"
      "BÜYÜK KÜÇÜK HARF DUYARLILIĞI OLACAKTIR.Parantez koymanız gereken yerlerde unutmayın.\n"
      "CEVAPLARI BİTİŞİK YAZINIZ (ZATEN SORULARIMIZ O ŞEKİLDE HAZIRLANMIŞ OLACAKLAR\n)"
      "KONUMUZ PYTHON PROGRAMLAMA DİLİDİR.\n\n")

time.sleep(2)

while True:
    baslamak = input("Hazırsanız başlayalım mı (evet / hayır) :")
    if baslamak == "evet":
        break
    else:
        continue

sonuc = 0
print(" SORU 1\n")
time.sleep(2)

print("Python programlama dilinde ekrana belirli bir mesaj yazdırmak için kullandığımız fonksiyon hangisidir ?\n ")
time.sleep(2)
print("LÜTFEN BÜYÜK KÜÇÜK HARF DUYARLILIĞINA DİKKAT EDİNİZ VE PARANTEZ GEREKİYORSA KOYMAYI UNUTMAYINIZ!\n")
time.sleep(2)
soru1cevp = input("SORU 1 İN CEVABINI GİRİNİZ :")
time.sleep(1)

if soru1cevp == "print()":
    sonuc += 10
    print("TEBRİKLER DOĞRU CEVAP\n\n\n\n")
else:
    print("MAALESEF YANLIŞ CEVAP.\n\n\n\n")

time.sleep(2)
print(" SORU 2\n")
time.sleep(2)
print("String metotlarından find('aranan şey') aranan şeyi bulamazsa ekrana hangi çıktıyı verir? \n")
time.sleep(2)
print("LÜTFEN BÜYÜK KÜÇÜK HARF DUYARLILIĞINA DİKKAT EDİNİZ VE PARANTEZ GEREKİYORSA KOYMAYI UNUTMAYINIZ!\n")
time.sleep(2)
soru2cevp = input("SORU 2 NİN CEVABINI GİRİNİZ :")

if soru2cevp == "-1":
    sonuc += 10
    print("TEBRİKLER DOĞRU CEVAP\n\n\n\n")
else:
    print("MAALESEF YANLIŞ CEVAP.\n\n\n\n")

time.sleep(2)
print(" SORU 3\n")
time.sleep(2)
print("Python programlama dilinde bir string değişkenin uzunluğunu veya listenin eleman sayısını veren fonksiyonun adı nedir ? \n")
time.sleep(2)
print("LÜTFEN BÜYÜK KÜÇÜK HARF DUYARLILIĞINA DİKKAT EDİNİZ VE PARANTEZ GEREKİYORSA KOYMAYI UNUTMAYINIZ!\n")
time.sleep(2)

soru3cevp = input("SORU 3 ÜN CEVABINI GİRİNİZ :")
if soru3cevp == "len()":
    sonuc += 10
    print("TEBRİKLER DOĞRU CEVAP\n\n\n\n")
else:
    print("MAALESEF YANLIŞ CEVAP.\n\n\n\n")

time.sleep(2)
print(" SORU 4\n")
time.sleep(2)
print("Python programlama dilinde kullanıcıdan komut almak için kullandığımız fonksiyon hangisidir? \n")
time.sleep(2)
print("LÜTFEN BÜYÜK KÜÇÜK HARF DUYARLILIĞINA DİKKAT EDİNİZ VE PARANTEZ GEREKİYORSA KOYMAYI UNUTMAYINIZ!\n")
time.sleep(2)
soru4cevp = input("SORU 4 ÜN CEVABINI GİRİNİZ :")

if soru4cevp == "input()":
    sonuc += 10
    print("TEBRİKLER DOĞRU CEVAP\n\n\n\n")
else:
    print("MAALESEF YANLIŞ CEVAP.\n\n\n\n")

time.sleep(2)
print(" SORU 5\n")
time.sleep(2)
print("numbers = [1,2,3,4,5]\n"
      "print(numbers[-1]\n"
      "               "
      "Yukarıdaki kodun çıktısı nedir ?\n")
time.sleep(2)
print("LÜTFEN BÜYÜK KÜÇÜK HARF DUYARLILIĞINA DİKKAT EDİNİZ VE PARANTEZ GEREKİYORSA KOYMAYI UNUTMAYINIZ!\n")
time.sleep(2)
soru5cevp = input("SORU 5 İN CEVABINI GİRİNİZ : ")

if soru5cevp == "5":
    sonuc += 10
    print("TEBRİKLER DOĞRU CEVAP\n\n\n\n")
else:
    print("MAALESEF YANLIŞ CEVAP.\n\n\n\n")
    
time.sleep(2)
print(" SORU 6\n")
time.sleep(2)
print("isim = 'Fatmanur Ömerli'\n"
      "a = isim[:10:2]\n"
      "yukardaki kodun çıktısı nedir ? \n")
time.sleep(2)
print("LÜTFEN BÜYÜK KÜÇÜK HARF DUYARLILIĞINA DİKKAT EDİNİZ VE PARANTEZ GEREKİYORSA KOYMAYI UNUTMAYINIZ!\n")
time.sleep(2)
soru6cevp = input("SORU 6 NIN CEVABINI GİRİNİZ : ")

if soru6cevp == "Ftau":
    sonuc += 10
    print("TEBRİKLER DOĞRU CEVAP\n\n\n\n")
else:
    print("MAALESEF YANLIŞ CEVAP.\n\n\n\n")

time.sleep(2)
print(" SORU 7\n")
time.sleep(2)
print("sayilar = [10,20,6,0,5,9,81,1000,23]\n"
      "result = max(sayilar)\n"
      "print(result)\n"
      "yukardaki kodun çıktısı nedir ?\n ")
time.sleep(2)
print("LÜTFEN BÜYÜK KÜÇÜK HARF DUYARLILIĞINA DİKKAT EDİNİZ VE PARANTEZ GEREKİYORSA KOYMAYI UNUTMAYINIZ!\n")
time.sleep(2)
soru7cevp = input("SORU 7 NİN CEVABINI GİRİNİZ : ")

if soru7cevp == "1000":
    sonuc += 10
    print("TEBRİKLER DOĞRU CEVAP\n\n\n\n")
else:
    print("MAALESEF YANLIŞ CEVAP.\n\n\n\n")

time.sleep(2)
print(" SORU 8\n")
time.sleep(2)
print("square = lambda num : num**2\n"
      "numbers = [1,2,3,9]\n"
      "result = list(map(square,numbers))\n"
      "print(result)\n"
      "yukardaki kodun çıktısı nedir ?\n ")
time.sleep(2)
print("LÜTFEN BÜYÜK KÜÇÜK HARF DUYARLILIĞINA DİKKAT EDİNİZ,\nLİSTEDE [ELEMAN, ]ŞEKLİNDE (ELEMAN VİRGÜLDEN SONRA BİR BOŞLUK OLSUN) VE PARANTEZ GEREKİYORSA KOYMAYI UNUTMAYINIZ!\n")
time.sleep(2)
soru8cevp = input("SORU 8 İN CEVABINI GİRİNİZ : ")

if soru8cevp == "[1, 4, 9, 81]" or "[1,4,9,81]":
    sonuc += 10
    print("TEBRİKLER DOĞRU CEVAP\n\n\n\n")
else:
    print("MAALESEF YANLIŞ CEVAP.\n\n\n\n")

time.sleep(2)
print(" SORU 9\n")
time.sleep(2)
print("1)def square(num):\n"
      "     return num**2\n"
      "2)def squre(num) : return num**2\n"
      "1 ve 2. öncüller eşittir.\n"
      "cevabınızı True veya False olarak giriniz\n")
time.sleep(2)
print("LÜTFEN BÜYÜK KÜÇÜK HARF DUYARLILIĞINA DİKKAT EDİNİZ VE PARANTEZ GEREKİYORSA KOYMAYI UNUTMAYINIZ!\n")
time.sleep(2)
soru9cevp = input("SORU 9 UN CEVABINI GİRİNİZ : ")

if soru9cevp == "True":
    sonuc += 10
    print("TEBRİKLER DOĞRU CEVAP\n\n\n\n")
else:
    print("MAALESEF YANLIŞ CEVAP.\n\n\n\n")

time.sleep(2)
print(" SORU 10\n")
time.sleep(1)
print("son sorumuz :)\n")
time.sleep(2)
print("Programlama dillerinde tüm dünyada ilk ekrana bastırılan kod nedir?\n")
time.sleep(2)
print("LÜTFEN BÜYÜK KÜÇÜK HARF VE BOŞLUK DUYARLILIĞINA DİKKAT EDİNİZ VE PARANTEZ GEREKİYORSA KOYMAYI UNUTMAYINIZ!\n")
time.sleep(2)
soru10cevp = input("SORU 10 UN CEVABINI GİRİNİZ : ")

if soru10cevp == ("Hello World") or ("hello world") or ("HELLO WORLD"):
    sonuc += 10
    print("TEBRİKLER DOĞRU CEVAP\n\n\n\n")
else:
    print("MAALESEF YANLIŞ CEVAP.\n\n\n\n")

time.sleep(2)
print("TEBRİKLER SORULARIMIZ BİTTİ.\n")
time.sleep(3)
print("SONUCUNUZ HESAPLANIYOR...................\n")
time.sleep(3)
print(f"{ad} {soyad} sonucunuz {sonuc}.Tebrik ederiz. ")
