def raju(a):
    if a == 4:
        return 1
    B=raju(a+1)
    print("hai")
    return B+2
res=raju(1)
print(res)  