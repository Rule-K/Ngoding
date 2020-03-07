#belajar Set atau Himpunan
#==============
Makanan = {"Sup Ayam","Opor Ayam","Ayam Kecap","Ayam-ayaman","Duh Ayam",
			"Ini kan Ayam"}
Minuman = set()
ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}
#==============
Makanan.add("Mari Beralih dari Ayam")
Makanan.add("Bebek Di makan Ayam")
Makanan.add("Sup Ayam")
Makanan.add("Opor Ayam")
#==============
Minuman.add("Teh manis")
Minuman.add("Kopi Hitam")
Minuman.add("Kopi Luwak")
Minuman.add("Teh manis")

#==============
print(Makanan)
print(Minuman)
print(sorted(Makanan))
print(sorted(Minuman))
print(ganjil)
print(genap)
print(ganjil.union(genap))
print(ganjil.intersection(genap))
print(ganjil.intersection(prima))
#=Sifat Indexing adalah Ketika ada data yang sama maka akan menjadi satu ada
##==============
