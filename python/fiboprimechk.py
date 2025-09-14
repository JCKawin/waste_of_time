import time

def primechk(a):
    if(a==1 or a==0):
        print("neither prime nor composite")
    else:
        i=2
        while i!=a:
            i+=1
            if(a%i==0 and i!=a):
                print("composite")
                break
        if(a==i):
            print("prime")

def fibo(n):
    a,b=1,0
    for i in range(0,n+1):
        c=a+b
        a=b
        b=c
        print(c)


start = time.time()      
a=int(input("enter no of terms"))
fibo(a)
print(f"{time.time() - start:.3f}")

