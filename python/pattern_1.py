n = int(input("N="))

lst: list[list[int]] = [[0]*n for _ in range(n)]
l:int = 0
i = u = 0
j = d = n-1
r = n
dir = (0,-1)

for k in range(n**2 , 0 , -1):
    lst[i][j] = k


    i += dir[0]
    j += dir[1]
   
    if j == l and i == u:
    
        r -= 1
        dir = (1,0)

    elif j == l and i == d:
   
        u += 1
        dir = (0,1)

    elif j == r and i == d:
        l += 1
    
        dir = (-1, 0)

    elif j == r and i == u:
 
        d -= 1
        dir = (0,-1)

    else : pass

    
for i in range(len(lst)):
        print(*lst[i] , sep = " " , end = "\n")


