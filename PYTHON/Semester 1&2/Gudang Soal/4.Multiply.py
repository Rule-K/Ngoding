n = int(input('Masukan salah satu angka dari 1 s/d 10 : '))

for h in range(1,11) :
	y = h*n
	print('Nilai dari {} dikali {} adalah {}'.format(h,n,y))