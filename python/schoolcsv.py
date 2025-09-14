import csv
csv.register_dialect("mydilect",skipinitialspace=True )
with open("C:\\Users\Kawin\Desktop\sample.csv",'w') as f:
    writer = csv.writer(f,dialect="mydilect")
    writer.writerows([["no","name"],[1,"kawin"],[2,"dahnush"]])


reader = csv.reader(open("C:\\Users\Kawin\Desktop\sample.csv",'r'))

array = []

for row in reader:
    array.append(row)

print(*array,sep="\n")





