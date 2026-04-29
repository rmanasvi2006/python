a=input("enter the password:")
up=0
sm=0
sp=0
dg=0
if len(a)>=8:
    for i in a:
        if i.isupper():
            up=up+1
        elif i.islower():
            sm=sm+1
        elif i.isdigit():
            dg=dg+1
    else:
        sp=sp+1
else:    print("password should be atleast 8 characters")
if up>0 and sm>0 and sp>0 and dg>0:
    print("strong password")
else:   
    print("weak password")
