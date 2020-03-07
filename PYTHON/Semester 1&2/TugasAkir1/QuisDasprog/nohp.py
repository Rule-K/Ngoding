nomorNya  = "00-44 48 5555 8361"
# Sedia box kosong
boxBaru   = ""
boxAkhir  = ""
hitungan  = 3
#Lakukan looping untuk seleksi tipe data
for x in range(len(nomorNya)):
	if nomorNya[x] == " " or nomorNya[x] == "-": # Melakukan seleksi untuk jenis data seperti dissamping 
		continue # Baru tau kemaren fungsi Continue untuk melewati index...
	else:
			boxBaru += nomorNya[x] # kalau sudah, masukan index yang tidak di lewati
			#Sekarang data sudah terseleksi sehingga spaci dan stip tidak ada

# looping box baru yg isisnya sudah terseleksi
for y in range(len(boxBaru)):
	if y != 0 : #supaya data di mulai dari 1
		if y % 3 == 0 : # seleksi setiap 3 digit
			boxAkhir += "-" #kemudian di tambah "-""

	boxAkhir+=boxBaru[y] #box akhir di tambahkan nilai box baru satu persatu

print("Nilai Awal : %s \nDi pisahkan : %s \nHasil akhit : %s "%(nomorNya,boxBaru,boxAkhir))