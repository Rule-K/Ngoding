import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

colors = ["Red","Green","Blue"]
explode = (0,0,0)
labels = ["Ini merah","Ini Hijau","Ini Biru"]
nums = [50,25,25]

fig, ax = plt.subplots()

def update(num):
    ax.clear()
    ax.axis('equal')
    str_num = str(num)
    for x in range(len(labels)):
        nums[x] += str_num.count(str(x))
    ax.pie(nums, explode=explode, labels=labels, colors=colors, 
            autopct='%1.1f%%', shadow=True, startangle=140)
    ax.set_title(str_num)

ani = FuncAnimation(fig, update, frames=range(len(labels)), repeat=True)
plt.show()