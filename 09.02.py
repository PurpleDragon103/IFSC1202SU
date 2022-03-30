def print_list(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ') 
        print()
def swap_columns(a, i, j):
    for row in range(len(a)):
        tmp = a[row][i]
        a[row][i] = a[row][j]
        a[row][j] = tmp
    return(a)

a = []
numfile = open("/workspace/IFSC1202SU/09.02 NumbersList.txt", 'r') 
num = numfile.readline() 

while num != "":
    y = num.split(" ")
    for i in range(len(y)):
        y[i] = int(y[i]) 
    a.append(y)
    num = numfile.readline()
numfile.close()

print_list(a)
swap = input("Enter the columns to swap: ")
s = []
s = swap.split(" ")
i = int(s[0])
j = int(s[1]) 

swap_columns(a, i, j)
print_list(a)