def convert(nilai,basis):
	kamus = "0123456789ABCDEF"
	if nilai < basis :
		return kamus[nilai]
	else :
		return convert(nilai//basis,basis) + kamus[nilai%basis]

nilainya = int(input("Masukan Nilainya dong : "))
dgBasis  = int(input("Basisnya Berapa.? : "))

print(convert(nilainya,dgBasis))