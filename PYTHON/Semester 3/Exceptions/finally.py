#finally
"""
Untuk Memastikan Kode tetap berjalan Apapun yang terjadi..
kita dapat menggunakan Statement #Finally

finally di letakan pada posisi terbahawah setela try dan except
sehingga finally berjalan setela 2 pernyataan tersebut

finally bahkan akan tetap bejalan walau pernyataan dalam block
except terdapat error!
"""
"""
try:
    print("Hello")
    print(1/0)
except ZeroDivisionError :
    print("Divided by Zero!")
finally:
    print("This code will run no matter What!!")

#There's an Rise Block Statement juga,
Ada Juga Assert cara pakainya

print(1)
assert 2+2 = 4
print(2)
assert 1 + 1 == 3
print(3)

resultnya
1
2
AssertionError
"""
try:
    print("Hello World")
    print(1/0)
except ZeroDivisionError :
    "Ada error lah Pokok!!"
    raise