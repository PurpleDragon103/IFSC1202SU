a = []
total = 0
# Open the file and read the first line 
tempsfile = open("/workspace/IFSC1202/Text Files/09.06 CityTemps.txt", 'r') 
temps = tempsfile.readline() 

while temps != "":
    y = temps.split(" ")
    for i in range(1,len(y)):
        y[i] = int(y[i]) 
    a.append(y)
    temps = tempsfile.readline()
tempsfile.close()

for i in range(len(a)):
    for j in range(1,len(a[i])):
        total += a[i][j]
    avg = total / (j-1)
    a[i].append(int(avg))
    total = 0

print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<}".format('City','Mo','Tu','We','Th','Fr','Sa','Su','Avg'))
# Print Process Loop
for i in range(len(a)):
    print(a[i][0], end='   ')
    for j in range(1,len(a[i])):
        print(a[i][j], end='       ')
    print()
