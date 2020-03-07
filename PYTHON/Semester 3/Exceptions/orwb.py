"""
File bertype teks supaya bisa di edit maka harus di buka dulu
#Untuk membuka file pada python kita bisa menggunakan

variabel = open("FileName.txt)
"""
#Sederhananya
myfile = open("text.txt")

"""
#OpenStyle

open("filename.txt","w") -- now i can re write the conten or the file
open("filename.txt","r") -- We can read the file, but it was the default, so dont need maybe
open("filename.txt","a") -- we adding new content to the end of file. du know why.?
open("filename.txt,"wb") -- or only "b",  used for non txt file like image or sound

#so Close it
example the variable name is "file" so :
file.close() -- to close the file

Reading files
-------
"""
teks = open("text.txt","r")
#for i in range(21):
    #print(file.read(4))
#print(file.read(4))
#file.close()
"""
Setelah semua konten telah di read, maka upaya untuk me read file lagi
akan memberikan string kosong karena kita mencoba untuk membaca dari akhir file
"""
#file.read()
#print("HAi")
#print(file.read())
#rint("Juga")
#file.close()
"""
Anda Juga bisa lo melakukan looping pada file yang di read, atau juga 
menggunakan statement .readlines() untuk membuatnya menjadi list
"""
#print(teks.readlines())
#atau
for line in teks:
    print(line)

# Now we start to writing file!!!!
"""
x = open("text.txt","w")

x.write("Ini Lagi nulis isi file sambil nyoba ngetik 10 jari tapi gak bisa-bisa")
x.close()

y = open("text.txt","r")
print(y.read())
y.close()
------------------
Ketika melakukan write pada fila yang di buka pada "w" mode, maka isi dari file sebelumnya akan di
replace oleh isi file yang baru kita tulis..

isi atau content juga terhapus walaupun anda hanya melakukan write mode ("w),
kemudian segera menutup tanpa merubah isi file..

melakukan write juga bisa di lakukan dengan cara unik di bawah ya..
perintah "msg" mungkin sama seperti len...
"""

msg = "Apalah dayaku ya allah!! :("

buka = open("text.txt","w")

ammount = buka.write(msg)
print(ammount)
buka.close()
