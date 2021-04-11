#day3 
oncedenBelirlenmisKullaniciAdi = input("bir kullanıcı adı belirleyiniz: ")
oncedenBelirlenmisSifre = input("bir şifre belirleyiniz : ")


kullaniciBilgileri = {
    "kullaniciAdi" : oncedenBelirlenmisKullaniciAdi,
    "sifre" : oncedenBelirlenmisSifre

}


while True:
    kullaniciAdiKontrol = input("Önceden belirlediğiniz kullanıcı adınızı giriniz: ")
    sifreKontrol = input("Önceden belirlediğiniz şifrenizi giriniz: ")

    if kullaniciAdiKontrol == kullaniciBilgileri["kullaniciAdi"] :
        if sifreKontrol == kullaniciBilgileri["sifre"]:
            print("Giriş başarılı")
            break
        else:
            print("HATALI ŞİFRE. LÜTFEN TEKRAR DENEYİNİZ.")
            continue
    else:
        print("HATALI KULLANICI ADI. LÜTFEN TEKRAR DENEYİNİZ.")
        continue


