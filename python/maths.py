import random

g = open("ans.txt", "w")
f = open("txt.txt", "w")
for i in range(136):
    while True:
        a = random.randint(2, 16)
        b = random.randint(2, 16)
        if (a-b)>0:
            f.write(f"{i + 1}. {a} x {b}=\n")
            g.write(f"{i + 1}. {a * b}\n")
            break
    
