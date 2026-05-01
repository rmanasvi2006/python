a = [[" " for i in range(11)] for i in range(11)]
for i in range(11):
    for j in range(11):
        if j == 0 or j == 10 or (i == j and i <= 4) or (i + j == 10 and i <= 4):
            a[i][j] = "*"
        else:
            a[i][j] = " "

for i in range(11):
    for j in range(11):
        print(a[i][j],end=" ")
    print()

