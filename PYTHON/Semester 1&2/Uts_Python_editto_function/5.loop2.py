def loop():    
    bil = [int(bil) for bil in input("Masukan bilangan, Pisahkan dengan spasi: ").split()]
    jml = 0
    for b in bil:
    	jml += b
    	b /= len(bil)
    print("Jumlah bilangan adalah %s dengan input %s buah, maka rata-rata %s"%(jml,len(bil),b))

loop()