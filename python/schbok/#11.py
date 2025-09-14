str = input()
setword = str.split(" ")
setword = set(setword)
for i in setword:
    print(f"No. of {i} = {str.count(i)} ")