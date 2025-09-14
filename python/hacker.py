import sty
import random
import time
import datetime 

print(f"{datetime.datetime.today(): %Y %B %d}")
a = input("Press enter to start HACKING")
time.sleep(5)
print("hacking...")
time.sleep(0.1)
print("On approx it takes 15 sec")
start = time.time()

time.sleep(3)
while True:
    string = sty.fg.green+f"{str(bin(random.randint(100000000000000000000000000000,999999999999999999999999999999999)))}"
    print(string.lstrip("0b1"))
    if round(time.time()-start)== 15.0:
        break

print("\n\n\n Hacked!")


