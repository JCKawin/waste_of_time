#decending order
a=[]
for i in range(10):
    a.append(int(input("enter a number=")))
a.sort()
b=[]
for g in range(10):
    b.append(a[9-g])
for j in b:
    print(j,end="\t")
