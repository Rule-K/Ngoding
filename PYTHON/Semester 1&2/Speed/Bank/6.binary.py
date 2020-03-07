import random
random = random.randint(1,100)
batas = 0
var = int(input('Saya Memikirkan Suatu Angka coba tebak.? '))
while var != random:
	batas += 1

if batas == 3 :
	print('Nilai Yang benar adalah %s'%random)
elif var > random :
	print('Angaka anda terlalu besar')
elif var < random :
	print('Angka Anda terlalu kecil')
elif var == random :
	print('Selamat Anda Benar')