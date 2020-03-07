def bagi(x):
	print("Anda memasukan angka: ",x)
	bag = x % 3
	# ini Genap atau Ganjil
	if x % 2 == 0 :
		print(x,"adalah bilangan genap")
	else:
		print(x,"Adalah Bilangan ganjil")
	# Apakah Habis di bagi 3 
	if bag == 0 :
		print(x,"Habis di bagi 3")
	else :
		print(x,"tidak habis di bagi 3, dengan sisa ",bag)

bagi(5)