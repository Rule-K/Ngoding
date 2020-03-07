var = int(input('Masukan Suatu Bilangan Brow : '))
jumlah = 0 
for v in range(1,var+1):
	vv = v ** 2
	jumlah = jumlah + vv
	print('Bilangan %s di Kuadratkan adalah %s'%(v,vv))
print()
print('Jumlah Semua Kuadrat adalah %s'%jumlah)