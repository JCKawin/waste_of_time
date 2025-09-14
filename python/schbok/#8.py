yr = int(input())
if yr%400==0:
    print("leap yr")
elif yr%4==0 and yr%100!=0:
    print("leap yr")
else:
    print("not a leap year")

