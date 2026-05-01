a=input("enter a guy name:")
b=input("enter a girl name:")
a1=list(a)
b1=list(b)
for i in range(len(a1)):
    for j in range(len(b1)):
        if a1[i]==b1[j]:
            a1[i]='2'
            b1[j]='2'
print(a1)
print(b1)
cnt=0
for i in a1:
    if i!='2':
        cnt=cnt+1
for i in b1:
    if i!='2':
        cnt=cnt+1
print(cnt)

index=0
for i in range(len(a1)):
    for j in range(len(b1)):
        if a1[i]==b1[j]:
            index=index+1
print(index)    
