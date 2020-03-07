var = int(input('Masukan Suatu Bilangan Brow : '))
va = var % 3 
print('Bilangan Input Adalah %s'%var)
if var % 2 == 0 :
	print('Bilangan %s Adalah Bilangan Genap'%var)
else:
	print('Bilangan %s Adalah Bilangan Ganjil'%var)

if var % 3 == 0 :
	print('Bilangan %s Habis di Bagi 3'%var)
else:
	print('Bilangan %s Tidak Habis di bagi 3 karena sisa %s '%(var,va))