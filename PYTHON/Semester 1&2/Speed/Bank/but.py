def jumlah_kuadrat(x):
	jum = 0
	for j in range(1,x+1):
		jum = jum + (j ** 2)
	return jum

hasil = jumlah_kuadrat(int(input('Masukan Bilangan : ')))
print('Jumlah dari Kuadrat Adalah ',hasil)