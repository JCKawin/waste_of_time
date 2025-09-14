#fibanocci serires
import sys

def fibo(n):
    a=0
    b=1
    if(n==0):
        print (a)
    elif(n==1):
        print (a)
        print (b)
    else:
        print ("1 - ",a)
        print ("2 - ",b)
        for i in range (3,n+1):
            c=a+b
            print (i," - ",c)
            a=b
            b=c
sys.set_int_max_str_digits(10000000)
a=int(input("enter the no. of. terms to be printed"))
fibo(a)
