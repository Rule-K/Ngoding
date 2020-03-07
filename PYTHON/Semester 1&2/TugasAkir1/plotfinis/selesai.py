# Import packages tapi banyakan yag gak bisa saya pakek
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np
# Read file na dulu
file      = pd.read_csv("jomblo18.csv") # fils CSV, berisa data wanita dan pria yg belum nikah
pria      = file.cowok #data cowok
wanita    = file.cewek # data cewe
camat_l     = file.kecamatanl # Kecamatannya
camat_p     = file.kecamatanp # Kecamatannya
#Variabel kosong untuk data nya
label_l    = []  #ini var buat kecamatan
label_p    = []
nums_l   = []  #Data Ceweknya
nums_p   = []  #list ceweknya
explode  = []  # Kalo Pie Biasanya pakek explode
explode_p = []
"""
#ini buar iseng aja tadi
jarak    = len(label) 
lebar    = 0.22
arangge  = np.arange(jarak)
#---
"""
y = 0 #Looping untuk isi explode, biar gak capek atu-atu
for ledak in range(len(camat_l)):
	x = "0"*len(camat_l)
	explode.append(int(x[y]))
	y += 1

for barru in range(len(explode)):
	explode_p.append(explode[barru]+1/3)

for laki in pria: # buat isi var list nums_l
	nums_l.append(laki)

for nine in wanita: # buat isi var list nums_p
	nums_p.append(nine)

for taok in camat_l: # buat isi var list Label
	label_l.append(taok)

for taok in camat_p: # buat isi var list Label
	label_p.append(taok)
#--
fig,ax = plt.subplots() #Sub plot
#--
"""
Abaikan saja ini
----------------
barnya_1 = ax.bar(arangge,nums_l,lebar,color="red")
barnya_2 = ax.bar(arangge+lebar,nums_p,lebar, color="Green")
"""
#--
def pie(): #pemanggilan filenya untuk pie 1 / laki - laki
	ax.clear()
	ax.axis("equal")
	ax.set_title("Para Pria dan wanita Jomblo")
	for x in range(len(label_l)):
		nums_l[x]
		nums_p[x]

	ax.pie(nums_p,explode=explode_p,labels=label_p,autopct="%1.1f%%",startangle=60)
	ax.legend(loc="upper left")
	ax.pie(nums_l,explode=explode,labels=label_l,autopct="%1.1f%%",startangle=60)

pie()
#ani = FuncAnimation(fig, pie2, frames=100, repeat=True)
#--
plt.show()
