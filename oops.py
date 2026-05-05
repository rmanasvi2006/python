class abc:
    num=100
    def set_dim(self,a,b):
        self.total=a+b+abc.num
    def display(self):
        print("addition is ", self.total)
a=abc()
b=abc()
a.set_dim(20,30)
b.set_dim(30,50)
a.display()
b.display()
