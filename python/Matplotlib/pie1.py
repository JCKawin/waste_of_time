import matplotlib.pyplot as plt

knowlegde = [50,60,12,49,32,12,50]

labels=["physics","computer","art","english","video games","cricket","maths"]

plt.pie(knowlegde,labels = labels , autopct="%.1f")

plt.show()

