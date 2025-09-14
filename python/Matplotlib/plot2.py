import matplotlib.pyplot as plt

data:list = [[1,2,3],[5,7,4],[2,10,5]]

plt.plot(data[0] , data[1] , label = 'line 1 ')
plt.plot(data[0] , data[2] , label = 'line 2')
plt.xlabel("kawin")
plt.ylabel("dahunush")
plt.title("line grtaph")
plt.legend()
plt.show()

