#Ada Beberapa cara dalam Melakukan Import Module

# Yang Pertama 1

import matematika 
print("-"*40)
matematika.kurang(4,3)

# Yang Kedua 2

import matematika as math
print("-"*40)
math.tambah(5,7)

# Yang Ketiga 3
from matematika import kali
print("-"*40)
kali(8,2)

"""Bisa Juga di tuliskan seperti ini
(from matematika import kali , bagi)
atau (from matematika import * )Artinya mengambil semuanya"""

# Yang Keempat 4
from matematika import bagi as b 
print("-"*40)
b(7,5)