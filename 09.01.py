
a = []
maxn = 0
row = 0
col = 0

x = input("Enter the number of rows and columns: ")
MofN = x.split(" ")
# Convert the values from string to an integer
for i in range(len(MofN)):
    MofN[i] = int(MofN[i])

# MofN has number of rows in 0 and columns in 1
for m in range(MofN[0]):
    data = input("Input a line of data: ")
    line = data.split(" ")
    # string to int conversion
    for num in range(MofN[1]):
        line[num] = int(line[num])
    # Append the list to the two dimensional array
    a.append(line)

# Loop through each row in the two dimensional array
for i in range(len(a)):
    # Loop though each element in the list
    for j in range(len(a[i])):
        if a[i][j] > maxn:
            maxn = a[i][j]
            row = i
            col = j

print("The maximum value {} occured in row {} column {}".format(maxn,row,col))


