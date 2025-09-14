import matplotlib.pyplot as plt
import random


class Particle:

    def __init__(self, num):
        self.x_val = [0]
        self.y_val = [0]
        self.num = num

    def simulate(self):
        while len(self.x_val) != self.num:
            direction = [1, -1]
            distance = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.x_val.append(self.x_val[-1] + (random.choice(direction) * random.choice(distance)))
            self.y_val.append(self.x_val[-1] + (random.choice(direction) * random.choice(distance)))


a: Particle = Particle(5000)
a.simulate()
plt.scatter(a.x_val, a.y_val, s=1 , cmap='Blues')
plt.show()
