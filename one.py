class geometric_shape:
    def __init__(self) -> None:
     self.l=10
     self.b=5
     self.pi=3.14
     self.r=4
     self.a=12
     self.c=10
     self.h=10
     
    def Rectangle_area(self):
       c= self.l*self.b
       print("The area of Rectangle = ",c)
   
   
    def Rectangle_prrimeter(self):
        c=2*(self.l+self.b)
        print("The perimeter of Rectangle = ",c)
    
class Subclass(geometric_shape):
    def Circle_peri(self):
        p=2*self.pi*self.r
        print("The perimeter of Circle =",p)
    
    def Area_of_Circle(self):
        A=2*self.pi*self.r**2
        print("The area of Circle = ",A)
    
    def Square_area(self):
        A=self.l*self.b
        print("The area of Square = ",A)
    
    def Square_perimeter(self):
        P=4*self.l
        print("The perimeter of Square = ",P)
    
    def Triangle_area(self):
        A=self.a+self.b+self.c
        print("The area of Triangle = ",A)
        
    def Triangle_perimeter(self):
        P= 1/2*self.c*self.h
        print("The perimeter of Triangle = ",P)
    
    
if __name__ == "__main__":  
    g1=Subclass()
    g1.Rectangle_area()
    g1.Rectangle_prrimeter()
    g1.Circle_peri()
    g1.Area_of_Circle()
    g1.Square_area()
    g1.Square_perimeter()
    g1.Triangle_area()
    g1.Triangle_perimeter()
    