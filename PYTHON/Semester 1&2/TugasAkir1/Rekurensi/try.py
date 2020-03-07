a = 7
b = 3

c = a / b
d = a // b
e = a % b
f = d > e
g = c < d
h = f and g
i = f or g
j = not i
k = c!= d
l = a*3
m = b**3

a = 'Seorang terpelajar harus sudah berbuat adil sejak dalam pikiran apalagi dalam perbuatan'
q = 'There is no greater wealth than wisdom, no greater poverty than ignorance; no greater heritage than culture and no greater support than consultation'
total = 0

Angka = 1000000
n1 = 0
n2 = 1
count = 2

if Angka <= 0:
   print("Angka harus di atas 0")
elif Angka == 1:
   print("Deret fibonacci : ",Angka,":")
   print(n1)
else:
   print("Deret fibonacci : ",Angka,":")
   print(n1,",",n2,end=', ')
   while count < Angka:
       nth = n1 + n2
       print(nth,end=' , ')
       # tukar nilai untuk mendapatkan 2 index terakhir
       n1 = n2
       n2 = nth
       count += 1
"""
a = [0 , 1, 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 ]
y = 0
for x in range(len(a)):
    if a[y] % 2 == 0 :
        print(a[y])
    y+=1
"""
"""
a = 0
for i in range(5):
  a = a + 1
  print(a)

b=0
for i in range(2,5):
  b = b + 1
  print(b)

c=0
for i in range(1,10,2):
  c = c + 1
  print(c)
"""


