a = []
FromValue = float(input("Enter From Value: "))
FromUnit = input("Enter From Unit (mm, cm, m, km, in, yd, mi): ")
ToUnit = input("Enter To Unit (mm, cm, m, km, in, yd, mi): ")
row = 0
col = 0
# Open the file and read the first line 
convfile = open("/workspace/IFSC1202/Text Files/09.04 Conversion.txt", 'r') 
conv = convfile.readline() 

while conv != "":
    y = conv.split(" ") 
    a.append(y)
    conv = convfile.readline()
convfile.close()

for i in range(1,len(a)):
    for j in range(1,len(a[i])):
        if a[i][0] == FromUnit:
            row = i
if row == 0:
    print("FromUnit is not valid")
    exit()
for i in range(1,len(a)):
    for j in range(1,len(a[i])):
        if a[0][j] == ToUnit:
            col = j
if col == 0:
    print("ToUnit is not valid")
    exit()

ToValue = (FromValue * float(a[row][col]))
ToValue = round(ToValue,7)

print("{} {} => {} {}".format(FromValue,FromUnit,ToValue,ToUnit))

