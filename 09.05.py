a = []
n = int(input("Enter Size: "))
for i in range(n+2):
    a.append([' '] * (n+2))

# corners
a[0][0] = '+'
a[0][-1] = '+'
a[n+1][0] = '+'
a[n+1][-1] = '+'
for i in range(1,n+2):
    # border lines
    a[0][i] = '-'
    a[i][0] = '|'
    a[n+1][i] = '-'
    a[i][n+1] = '|'

# inside
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i % 2) == 0 and (j % 2) != 0:
            a[i][j] = '*'
            a[j][i] = '*'

# print the picture 
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ') 
    print()
