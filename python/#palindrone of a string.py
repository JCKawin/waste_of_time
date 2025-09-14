s=input()
s=list(s)
b=[]
for i in range(1,len(s)+1):
    b.append(s[len(s)-i])
e=''
f=''
d=e.join(s)
h=f.join(b)
if d==h:
    print("palindrome")
else:
    print("not a palindrome")
