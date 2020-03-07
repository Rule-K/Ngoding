#kumpulan def
#=============
#Jumlah setiap bilangan 
def sum_it(list):
    total = 0
    total2 = 0
    for l in list:
        kuadrat = int(l)**2
        total += int(l)
        total2 += kuadrat
        rata = total / len(list)
    return total,rata , total2
#Bilangan Terkecil

#Menghitung nilai terbesar dari input split
def besar_kecil(list):
    B = min(list)
    K = max(list)
    return B,K
    #jumlah = 0
    #for i in list :
     #   if jumlah > int(i) :
      #      jumlah = int(i)
    #return jumlah
#==========
#Function ke Variabel
#==========
print("="*60)
jumjum = input("Masukan dengan spasi: ").split()
hasil_sumit = sum_it(jumjum)
sarcil = besar_kecil(jumjum)
#==========
#print hasil def
#==========
print("="*60)
print("1. Jumlah data  %s dengan rata-rata %s, dan jumlah kuadrat %s"%(hasil_sumit))
print("2. Nilai terkecil dari input adalah %s dan Terbesar %s"%(sarcil))
print("="*60)