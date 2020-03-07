#Exeption -> An even that Occurs due to incorect code or input
"""
print("7"+4)
akan mengeluarkan message TypeError
"""
#Exept Handling
"""
untuk mengatasi code exception, kita bisa menggunakan statement Try/except
try mungkin untuk menampikan pesan exception..

maksudnya jika kode yang berada di try sudah di jalankan kemudian terjadi error
maka kode yang berada di blok except yang akan di jalankan..
contoh
--------------------
try:
    num1 = 7
    num2 = 0
    print(num1/num2)
    print("Done Calculator")
except ZeroDivisionError:
    print("An error occurred")
    print("Due to zero Division")

resultnya :
An error occurred
due to zero Division
-----------------------
Block Except bisa lebih dari satu..
kemudian jika setelah perintah TRY hanya ada perintah Except tanpa 
ada tambahan Zero division error atau yg lain maka
except Akan megoreksi semua jenis error pada Program..
"""