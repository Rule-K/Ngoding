import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
# membuat variabel
dataNya   = pd.read_csv("countries.csv")
#---
egypt     = dataNya[dataNya.negara == "Egypt"]
ecuador   = dataNya[dataNya.negara == "Ecuador"]
argentina = dataNya[dataNya.negara == "Argentina"]
angola    = dataNya[dataNya.negara == "Angola"]
#---
jarak     = len(egypt.tahun)
xjarak    = np.arange(jarak) # lokasi x untuk sub plot nya
lebar     = 0.23 # lebar barnya

gambar = plt.figure()
ax     = gambar.add_subplot(111) # kurang tau fungsinya apa

mesir_p     = egypt.populasi/10**6
ecuador_p   = ecuador.populasi/10**6
argentina_p = argentina.populasi/10**6
angola_p    = angola.populasi/10**6
#--- Set chartnya
barnya_1 = ax.bar(xjarak,ecuador_p,lebar,color="red")
barnya_2 = ax.bar(xjarak+lebar,argentina_p,lebar, color="Green")
barnya_3 = ax.bar(xjarak+lebar*2,mesir_p,lebar,color="Blue")
barnya_4 = ax.bar(xjarak+lebar*3,angola_p,lebar,color="Yellow")
#--- Kasi Labelnya dulu doong
ax.set_ylabel("Pertumbuhan Penduduk")

plt.show()