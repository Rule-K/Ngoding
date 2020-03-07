import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import pandas as pd 
import numpy as np
#---
file      = pd.read_csv("jomblo18.csv")
pria      = file.cowok
wanita    = file.cewek
camat     = file.kecamatan
#---
label    = []
nums_l   = []
nums_p   = []
explode  = []
#---
y = 0
for ledak in range(len(camat)):
	x = "0"*len(camat)
	explode.append(int(x[y]))
	y += 1

for laki in pria:
	nums_l.append(laki)

for nine in wanita:
	nums_p.append(nine)

for taok in camat:
	label.append(taok)
#--
fig,ax = plt.subplots()
def anime(num):
	ax.clear()
	ax.axis("equal")
	for x in range(len(label)):
		nums_l[x]
	ax.pie(nums_l,explode=explode,labels=label,autopct="%1.1f%%")
#--
ani = FuncAnimation(fig, anime, frames=range(len(label)), repeat=True)
plt.show()