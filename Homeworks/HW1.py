# day2 soru 1

#yöntem1
liste = ['e1','e2','e3','e4','e5','e6','e7','e8','e9','e10']
kisimBir = liste[0:5]
kisimIki = liste[5:10]
kisimBir,kisimIki = kisimIki , kisimBir
print(f"kısım bir :{kisimBir}\nkısım iki : {kisimIki}")
print( "ilk yarısı ile ikinci yarısı değiştirilmiş liste:" ,kisimBir + kisimIki)

#yöntem2

liste = [1,2,3,4,5,6,7,8,9,10]
listeyarim1= []
listeyarim2=[]

for i in range(1,11):
    if i <= 10/2:
        listeyarim2.append(i)
    elif i > 10/2 :
        listeyarim1.append(i)

degistirilmislist = listeyarim1 + listeyarim2

print(degistirilmislist)



#day2 soru 2
while True :
    sayi = int(input("Bir tek sayı giriniz --> "))
    if sayi % 2 != 0 :
        break

liste = []
for i in range(sayi):
    if i % 2 == 0 :
        liste.append(i)
print(liste)



