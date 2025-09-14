a = int(input())
b = int(input())
c = int(input())
if a<b and a<c:
    g = a
elif b<c and b<a:
    g = b
else:
    g = c 
print("the smallest value is ", g)


