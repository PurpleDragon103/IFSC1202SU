def print_list(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ') 
        print()
def scale_list(a, s):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] *= s
    return(a)

a = []
numfile = open("/workspace/IFSC1202SU/09.03 NumbersList.txt", 'r') 
num = numfile.readline() 

while num != "":
    y = num.split(" ")
    for i in range(len(y)):
        y[i] = int(y[i]) 
    a.append(y)
    num = numfile.readline()
numfile.close()

print_list(a)
s = int(input("Enter scale value: "))
scale_list(a, s)
print_list(a)
