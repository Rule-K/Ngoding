def bil(nilai):
    bil1=0
    for a in range(1,nilai+1):
        bil1+=a
    return bil1
i=int(input('masukkan angka yang anda mau :')) 
print('jumlah keseluruhan nilaimya adalah :', bil(i))

def bil(nilai):
    a=0
    b=0
    for i in range(1,nilai+1):
        b=i*i
        a+=b
        print(a)
    return a
x=int(input('masukkan angka yang amda mau :')) 
print('jumlah bilangan faktorial adalah :', bil(x))

def nilai_max(list):
    max=0
    for i in list:
        if max<int(i):
            max=int(i) 
    return max
input_nilai=input('masukkan angka pisahkan dengan spasi :') 
hasil=input_nilai.split()
print('nilai maximumnya adalah :', nilai_max(hasil))


def nilai_bawah(list_masukan):
	usia_min=int(list_masukan[0])
	for i in range(1,len(list_masukan)):
		usia=int(list_masukan[i])
		if usia_min>usia:
					usia_min=usia
	return usia_min
nilai=input('masukka. nilai pisahkan dengan spasi :')
hasil=nilai.split()
print('nilai minimalnya adalah :', nilai_bawah(hasil))

def rata_rata(list):
			nilai=0
			jumlah=0
			for x in list:
						nilai= nilai + int(x)
						jumlah+=1
			total=nilai/jumlah
			return total
input_nilai=input('masukkan angka pisahkan dengan spasi :') 
hasil=input_nilai.split()
print('nilai rata-ratanya adalah :', rata_rata(hasil)) 

