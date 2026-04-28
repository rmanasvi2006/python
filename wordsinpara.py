a=input("enter any sentence: ")
c=0
for i in range(len(a)):
  if a[i]==" " and a[i+1]!=" ":
    c+=1 
print("no. of words in the sentence: ",c+1)
