import random
import matplotlib.pyplot as pyt
lst = [random.randint(1,50) for i in range(50)]

fig , ax = pyt.subplots()

ax.plot(lst)
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.grid()
ax.legend("datas")
ax.set_title("kawin")



pyt.show()

