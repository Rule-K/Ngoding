def akar(x):
	print("Bilangan input adalah ",x)
	jumlah = 0
	for b in range(1,x+1):
		c = b ** 2
		jumlah += c
		print("%s akar 2 adalah %s"%(b,c))
	print("Bila setiap hasil di jumlahkan adalah ",jumlah)

akar(3)