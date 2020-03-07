def fusi(m,n):
	if n == 1 :
		return m
	else :
		return m * fusi(m,n -1)

nilai = int(input("Masukan Nilai Pertama: "))
nilaiTwo = int(input("Masukan Nilai Kedua: "))
print(fusi(nilai,nilaiTwo))