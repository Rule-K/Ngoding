nilai     = [1, 0, 0, 1, 0, 0]
masuk = int(input("Masukan Nilai: "))
hitung = []
bank = []
a = 0
for i in range(len(nilai)) :
	if nilai[i] == masuk :
		nilai[i] = masuk
		hitung.append(nilai[i])

for j in range(len(hitung)):
	bank.append(hitung[j])

for k in range(len(hitung)):
	bank.append(masuk)

print("Nilai sebelum : %s \nBanyak Berubah: %s \nData Baru: %s"%(nilai,len(hitung),bank))
"""
Pusing ah Pusing :(, maaf jarang ngoding
"""