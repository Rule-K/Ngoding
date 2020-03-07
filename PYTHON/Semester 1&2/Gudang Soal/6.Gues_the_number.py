import random

number = random.randint(1,100)

nama = input('Masukan nama anda: ')
print('Hai %s Selamat Datang.'%nama)
print('Saya Punya angka dari kisaran 1 s/d 100.')
while True :
	num = int(input('Coba tebak Angka berapa itu : '))

	if num < number :
		print('Angaka Anda terlalu kecil, silahkan coba lagi')
	elif num > number :
		print('Angka Anda terlalu besar, silahkan coba lagi')
	elif num == number :
		print ('Selamat Anda Berhasil')
		break
