def fibbo(x):
	if x <= 2 :
		return 1
	else :
		return fibbo(x - 2) + fibbo(x - 1)

nilai = int(input("Masukan Nilai: "))
print(fibbo(nilai))