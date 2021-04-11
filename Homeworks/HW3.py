ogrenciler = {}
ogrSayisi = int(input("Kaç öğrenci bilgisi gireceksiniz (önerilen 5): "))
count = 0
while True:
    kacinciOgr = input("Kaçıncı öğrenciyi giriyorsunuz (örneğin öğrenci1 - öğrenci2) : ")
    ogrAd = input("Öğrenci adını giriniz : ")
    ogrSoyad = input("Öğrenci soyadını giriniz : ")
    ogrNum = int(input("Öğrenci numarasını giriniz : "))
    midterm = int(input("Öğrenci midterm notunu giriniz : "))
    project = int(input("Öğrenci project notunu giriniz : "))
    final = int(input("Öğrenci final notunu giriniz : "))
    ogrenciler.update({
        kacinciOgr: {
            "ad": ogrAd,
            "soyad": ogrSoyad,
            "ogrenciNum": ogrNum,
            "midterm": midterm,
            "project": project,
            "final": final
        }
    })
    count += 1

    if count == ogrSayisi:
        break


print(ogrenciler)


notSozluk = {}
ogrBilgi = ogrenciler.values()
isimlist = []
soyadlist = []
numlist = []
passingGradelist = []
sayac = 0
for i in ogrBilgi:
    passingGrade = i["midterm"] * (0.3) + i["project"] * (0.3) + i["final"] * (0.4)
    passingGradelist.append(passingGrade)
    isimlist.append(i["ad"])
    soyadlist.append(i["soyad"])
    numlist.append(i["ogrenciNum"])


sonList = list(zip(isimlist, soyadlist, numlist, passingGradelist))

grades = []
for fno in sonList:
    grades.append(fno[3])
grades = sorted(grades, reverse=True)
uzunluk = len(grades)
print("Ad\t\t\t\t\tSoyad\t\t\t\tNum\t\t\t\tPassingGrade\n")
while uzunluk > 0:

    for satir in sonList:
        if uzunluk == 0:
            break
        if grades[0] == satir[3]:

            for indexs in satir:
                print(str(indexs), end='\t\t\t')
            print()
            grades.remove(grades[0])
            uzunluk -= 1


print("Sıralanmış öğrenci listesi : ", sonList)
