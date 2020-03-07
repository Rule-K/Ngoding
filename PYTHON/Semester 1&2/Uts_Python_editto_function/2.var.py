def kuadrat(x):
   return x,x**2,x**3
#Dibawah ni adalah perintah Inputnya
print("-="*50)

hasil = kuadrat(int(input("Bilangan: ")))
print("Bilangan input adalah %s, Kuadrat %s, pangkat 3 adalah %s"%(hasil))