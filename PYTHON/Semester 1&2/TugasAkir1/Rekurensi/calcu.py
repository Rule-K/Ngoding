def fac(n):
	if n == 0 :
		return 1
	else :
		return n * fac(n - 1)

def convert(nilai,basis):
	kamus = "0123456789ABCDEF"
	if nilai < basis :
		return kamus[nilai]
	else :
		return convert(nilai//basis,basis) + kamus[nilai%basis]
#======
print("=="*20)
nama = input("Hai! Tolong Masukan nama anda: ")
print("=="*20)
input("Catatan: \n Apabila program berhenti seperti ini tanpa perintah.. Maka Tekan ENTER!")
print("--"*20)
print("Hai %s, Ini adalah program kalkulator \n ada beberapa jenis kalkulator yang tersedia.."%(nama))
input("Diantaranya : \n 1. kalkulator Factorial \n 2. Converter")
print("=="*20)
input("Yang pertama keluar adalah program Factorial\n jadi silahkan isi angka dari nila Factorial yang anda cari.. ^_^")
#=======
print("=="*20)
facto = int(input("Masukan angka dari nilai yang anda cari : "))
fac_n = fac(facto)
#=======
print(" Nilai Faktorial dari %s adalah : \n---------------\n  %s \n---------------"%(facto,fac_n))
print("=="*20)
input("Silahkan tekan Enter... ")
print("--"*20)
input("Berikutnya dan yang terakhir!! \n Ini adalah Converter, yang berfungsi untuk \n merubah angka yang anda masukan..")
print("Dengan Catatan : \n1. Masukan nilai 2 pada gaya, untuk bilangan integer Cth: 10001")
input("2. Masukan 9 untuk bilangan 0 - 9")
input("3. Masukan 16 untuk Huruf Dan angka...")
input("Walaupun Sebenarnya Anda bisa memasukan gaya dari 0 - 20,\ndi harapakan jangan lebih.. ")
print("=="*20)
nilai = int(input("Masukan Nilai yang ingin di Ubah: "))
basis = int(input("Masukan Gaya: "))
convert = convert(nilai,basis)
print("Hasil Converter dar %s adalah: \n---------------\n %s  \n---------------\n"%(nilai,convert))
input("Tekan ENTER Untuk Keluar.. Terima Kasih.. %s ^_^"%(nama))
print()