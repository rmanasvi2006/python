def raju(a):
    if a ==1:
        return
    a -= 1
    raju(a)
    print("hai")
    raju(a)
raju(5)