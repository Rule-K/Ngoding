import numpy as np
import matplotlib.pyplot as plt

data1 = [50]
data2 = [30]
line = 4
#--------------------------
panjang = np.arange(len(data1))  
lebar = 0.5 
#--------------------------
gambar, ax = plt.subplots()
rects = ax.bar(panjang - lebar,data1, line, yerr=data1,
                color='Green', label='data1')
rects2 = ax.bar(panjang - lebar, data2,line, yerr=data2,
				color="Blue", label="data2")

plt.show()