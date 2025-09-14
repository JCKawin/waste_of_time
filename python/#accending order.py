#accending order
a = []
for i in range(10):
    a.append(int(input("enter a number=")))
a.sort()
for j in a:
    print(j, end="\t")
