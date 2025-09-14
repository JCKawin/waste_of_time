import random
import matplotlib.pyplot as plt

maxima_list  = [random.randint(0,10) for _ in range(5,10)]

print(maxima_list)

maxima = []

for i in range(1 , len(maxima_list)-1):
    if maxima_list[i-1] < maxima_list[i] and maxima_list[i] > maxima_list[i+1]:
        maxima.append((i,maxima_list[i]))

plt.plot(list(range(10)) , maxima_list)


print(maxima)

plt.show()