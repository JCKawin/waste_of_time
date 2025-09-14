import math


rows = int(input())

row  = ''
print("1".center(rows,' '))
for n in range(1 , rows +1):
    for r in range(0,n+1):
        row += f"{math.comb(n,r)}"
    print(row.center(rows,' '))
    row = ''
    print()



