legs=int(input("enter the number of legs: "))
heads=int(input("enter the number of heads: "))
flag=False
for cows in range(0,heads+1):
    hens=heads-cows
    cal_legs=cows*4 + hens*2
    if cal_legs==legs:
        flag=True
        break
if flag:
    print("cows:",cows)
    print("hens:",hens)
else:
    print("no solution")

