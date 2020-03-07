import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
# Membuat variable
file        = pd.read_csv("nikah.csv") #baca File CSV nya duluh..
nikah = file[file.status == "Nikah"] #
tahun12 = file[file.tahun == "2012"]
#Variabel kosong
daerah = [] #buat daftar daerahnya di pisah dulu lah
daerah_2012 = []
jumlah_nikah = [] # ini buat tua' dan inak' yang sudah nikah
tahun = [] # Mudahan gak ketumpuk yang sama jak..
#
for i in nikah.daerah : #
	daerah.append(i) # masukin daftar Daerah nya... yang masuk malah ketumpuk

for j in nikah.jumlah :
	jumlah_nikah.append(j)

for k in nikah.tahun :
	tahun.append(k)

for l in tahun12.daerah :
	daerah_2012.append(l)

# Mudahan Bisa Jadi Plot
labels = daerah
nums   = []
explode = []
#loop
y = 0
for l in range(len(daerah)):
	x = "0"*len(daerah)
	explode.append(int(x[y]))
	y += 1

t = 0
for s in range(len(jumlah_nikah)):
	if jumlah_nikah[s] == "-":
		continue
	else:
		nums.append(int(jumlah_nikah[s]))

print(daerah_2012)
# Bismillah
"""
plt.axis("equal")
plt.pie(nums , explode=explode, labels=labels,autopct="%1.1f%%")
plt.show()
"""