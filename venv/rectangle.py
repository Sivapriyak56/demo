class Rectangle:
    def _init_(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return (self.length*self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))
a=int(input("enter a number"))
b=int(input("enter a number"))
r1=Rectangle(a,b)
#r2=Rectangle()
#print(r1.area())
print(r2.area())
print(r1.perimeter())
#print(r1.perimeter())
