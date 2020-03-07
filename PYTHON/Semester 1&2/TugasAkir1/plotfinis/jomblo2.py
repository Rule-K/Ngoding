import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import pandas as pd 
import numpy as np
#---
file           = pd.read_csv("jomblo182.csv")
keruak         = file.keruak
sakra          = file.sakra               
terara         = file.terara    
sikur          = file.sikur	
masbagik       = file.masbagik	
sukamulia      = file.sukamulia	
selong         = file.selong	
pringgabaya    = file.pringgabaya	
aikmel         = file.aikmel	
sambelia       = file.sambelia	
montonggading  = file.montonggading	
pringgasela    = file.pringgasela	
suralaga       = file.suralaga	
wanasaba       = file.wanasaba	
sembalun       = file.sembalun	
suela          = file.suela	
labuhanhaji    = file.labuhanhaji	
sakratimur     = file.sakratimur
sakrabarat     = file.sakrabarat
jerowaru       = file.jerowaru
lenek          = file.lenek
#---
mepet  = [0.05,0]
labels = ["Wanita","Pria"]
camat  = [keruak,sakra,terara,sikur,masbagik,sukamulia,selong,pringgabaya,aikmel,sambelia,montonggading
		  ,pringgasela,suralaga,wanasaba,sembalun,suela,labuhanhaji,sakratimur,sakrabarat,jerowaru,lenek]
#---

fig, ax = plt.subplots()
def update(isinya):
	ax.clear()
	ax.axis("equal")
	for i in range(len(camat)):
		ax.pie(camat[i],explode=mepet,labels=labels,autopct="%1.1f%%",startangle=90)
	ax.set_title(i)

#plt.pie(keruak,explode=mepet,labels=labels,autopct="%1.1f%%",startangle=90)
ani = FuncAnimation(fig, update, frames=range(len(camat)), repeat=True)
plt.show()