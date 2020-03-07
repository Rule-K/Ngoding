# ini Tugas nomor 1
print('1.Hello world')
# dibawah tugas nomor 2
hello = ('2.Hello world, dengan Variabel')
print(hello)
#Dibawah Tugas Nomor 3
saya,saya1,saya2 = ('Nahrul','Khayattullah','Nahrul Khayattullah')
print('3.Hai %s Apa kabar.?'%saya2)
#Di bawah Tugas nomor 4
user = input('4.Siapa nama user : ')
print('	   Hai %s apa kabar juga.?'%user)
# Di bawah tugas nomor 5 variabel yang di pakai adalah var nomr 5
if saya == user or saya1 == user or saya2 == user :
	print('5.Hai Tuanku Apa kabar lagi.. XD')
elif saya != user:
	print('5.Sayang sekali ya, saudara %s, namun tuan %s lah tuan saya' %(user,saya))
#Dibawah ini Tugas nomor  6 var yang di pakai adalah var di atasnya juga
born = int(input('Tahun Berapa %s Lahir: '%user))
now = int(input('Tahun Berapa Sekarang: '))
old = now - born

if old >= 40 :
	print('6.usia %s sekitar %s tahun, Buruan tobat deh'%(user,old))
elif old >= 30 :
  	print('6.Usia %s Sekitar %s tahun, Masih Kuat Tapi cepet tobat lebih baik'%(user,old))
elif old >= 15 :
	print('6.Usia %s Masih seger. Tapi tobatlah anak muda.. karena allah sukeee..'%(old))
elif old < 15 :
	print('6.usia %s masih bocah, gak usah pacaran, rajin2 ngaji sono.'%old)
#Di bawah ini tugas Nomor 7
bil = int(input('Masukan Suatu Bilangan, Terserah Anda: '))
print('7.Bilangan Akan di cetak dari angka 1 sampai dengan angka yang kamu masukan '+user)
for a in range(1,bil+1) :
	print(a , end =' ')
print()
#Di bawah ini tugas Nomor 8
print('8.Bilangan Kelipatan 3 adalah Bilangan yang jika di bagi 3 adalah nol.. maka :')
for b in range(3,bil+1,3):
	print(b, end =' ')
#Di bawah ini adalah tugas nomor 9
print()
print('9. Bilangan kelipatan 3 dan juga termasuk dalam kelipatan 7 namun di mulai dari angka 1 maka :')
for c in range(1,bil+1,3):
	print(c, end=' ')
#Di bawah ini adalah tugas nomor 10
jumlah0 = 0

for d in range(1,bil+1) :
	jumlah0 = jumlah0 + d

print('')
print('10.Jumlah dari bilangan 1 sampai dengan %s adalah: %s'%(bil,jumlah0))
#Di bawah ini adalah Tugas nomor 11
jumlah1 = 1
for e in range(1,bil+1):
	f = e * bil
	jumlah1 = jumlah1 * e
	print('jika %s dikali %s maka hasilnya: %s'%(e,bil,f))
	print()
	print('Jumlah kali-kalian dari Bilangan %s adalah : %s'%(e,jumlah1))
# Tugas di bawah ini adalah tugas nomor 12

# Tugas Di bawah ini tugas nomor 13
jumrata = [int(jumrata) for jumrata in input("Masukan bilangan, pisahkan dengan spasi: ").split()]
for j in jumrata :
	jumlah0 += j
	rata = jumlah0 / len(jumrata)

print('Jumlah %s bilangan adalah %s dan Rata-ratanya adalah %s'%(len(jumrata),jumlah0,rata))