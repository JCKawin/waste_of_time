#decen_fibo_primchk
def pc(a):
    i=2
    if (a==0 or a==1):
        return "N"
    while i!=a:
        if a%i==0:
            return "C"
        i+=1
    if a==i:
        return "P"
y=int(input("enter the no of values="))
s=[]
r=[]
a,b=0,1
print("\n processing...")
for d in range(y):
    print(a,sep=',')
    s.append(a)
    c=a+b
    a=b
    b=c
print("\n processing...")
print("total list=",s)
for f in range(1,y+1):
    r.append(s[y-f])
print("\n processing...")
print("reverse list=",r)
print("\n processing...")
print("final output")
for h in r:
    print(h,pc(h))
    
    
