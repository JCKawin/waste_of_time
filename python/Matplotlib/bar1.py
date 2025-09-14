import matplotlib.pyplot as plt

labels = ["Tamil","English","maths","Physics","Chemistry","Computer"]
marks = [73,92,96,91,87,95]

plt.bar(range(len(labels)), marks)
plt.xticks(range(len(labels)),labels)
plt.ylabel("marks")
plt.title("Quarterly Marks")

plt.show()

