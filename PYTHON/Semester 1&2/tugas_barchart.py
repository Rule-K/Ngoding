# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 06:45:38 2019

@author: Rules
----
Tugas Besar--- Menggunakan mathplotlib -- dengan barchart
----
"""

import numpy as np
import matplotlib.pyplot as plt

klu, klu_std = [72], [1]
klb,klb_std = [9],[1]
ktim,ktim_std =[2],[1]
klt,klt_std = [2],[1]
mataram,mataram_std = [4],[1]
bali,bali_std = [2],[1]
jumlah,jumlah_std = [91],[1]
#--------------------------
ind = np.arange(len(klu))  # the x locations for the groups
width = 1  # the width of the bars
#--------------------------
fig, ax = plt.subplots()
rects7 = ax.bar(ind - width/3, jumlah, width, yerr=jumlah_std,
                color='Grey', label='jumlah')
rects1 = ax.bar(ind - width/5, klu, width, yerr=klu_std,
                color='Red', label='Lombok Utara')
rects2 = ax.bar(ind + width/6, klb,width,yerr=klb_std,
                color='Blue', label='Lombok Barat')
rects3 = ax.bar(ind - width/5, klt, width, yerr=klt_std,
                color='yellow', label='Lombok Tengah')
rects4 = ax.bar(ind - width/1, ktim, width, yerr=ktim_std,
                color='brown', label='Lombok Timur')
rects5 = ax.bar(ind + width/1, mataram,width,yerr=mataram_std,
                color='green', label='Mataram')
rects6 = ax.bar(ind - width/2, bali, width, yerr=bali_std,
                color='orange', label='Bali')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Korban Jiwa / Orang Meninggal')
ax.set_title('Gempa Lombok, Minggu 5 Agustus 2018')
ax.set_xticks(ind)
ax.set_xticklabels(('Data Dari Kompas.Com'))
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")
autolabel(rects3, "center")
autolabel(rects4, "left")
autolabel(rects5, "right")
autolabel(rects6, "center")
autolabel(rects7, "left")

plt.show()
