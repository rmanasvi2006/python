a=1
for i in range(2,5):
    a=a+i
    for j in range(i):
        a=a+j
        print(str(a),end="")
    print()
print(a)
