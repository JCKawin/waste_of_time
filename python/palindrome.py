import time

print("hello")
a=input()
a=list(a)
b=a[:]
b.sort(reverse=True)

if a==b:
    print("Analaysing your text")
    time.sleep(3)
    print("palindrome")
else:
    print("Analaysing")
    time.sleep(3)
    print("Not a palindrome")
