#teknik Looping
#=================
#Variabel di sini
temen_oe = ["Hery",
            "Bang Sahril",
            "Jaka",
            "Asqolani",
            "Ten",
            "Feni",
            "Wahyu",
            "alpin"]
tingginya = [160,
             170,
             160,
             163,
             171,
             170,
             "Gak Tau",
             161]
iterasi = 0
kartun = {"Global TV":"Spongebob",
          "MNC TV":"Upin & Ipin",
          "RTV":"Bus Kecil Tayo"}
#=================
#Ini Eksekusinya
#=================
for temen in temen_oe:
    iterasi += 1
    print(iterasi,temen)
#=================
print("="*60)
print("Dengan Enumerate")
print("="*60)
#=================
for i,temenan in enumerate(temen_oe):
    print(i,temenan)
#=================
print("="*60)
print("looping Dengan Zip")
print("="*60)
#=================
'''Kalau di kedua  List Nggak ada temennya maka, si looping
tidak akan menampilkan data list yang nggak punya pasangan'''
for temen,tinggi in zip(temen_oe,tingginya):
    print("%s itu tingginya %s"%(temen,tinggi)) 
#=================
print("="*60)
print("Dengan Dictionary")
print("="*60)
#=================
for k,v in kartun.items():
    print("di %s ada Kartun %s"%(k,v))
print("="*60)
#Kalau Tanpa tanda Koma di k,v -> k
for k in kartun.items():
    print(k)