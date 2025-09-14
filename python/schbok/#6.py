a = int(input())
y = a
div = 0
while a!=0:
    rem = a%10
    div = div*10 + rem
    a=a//10  
print(div)
if y == div:
    print("palindrome")
else:
    print("not a palindrome")

