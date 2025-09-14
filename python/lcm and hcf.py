a=int(input())
b=int(input())
if a>=b:
    m,n=a,b
else:
    m,n=b,a
h=0
while m%n!=0:
    h=m%n
    m=n
    n=h
l=int((a*b)/n)
print("The given numbers are",a,",",b)
print("Hcf=",n)
print("Lcm=",l)
