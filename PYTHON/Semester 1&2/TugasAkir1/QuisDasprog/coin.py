longData = int(input("Masukan Jumlah Data anda : "))
data = []
for i in range(0,longData+1) :
	data[i].append(int (input("masukan data  = ")))
for x in range(0,len(data)+1) :
	print (data[x])