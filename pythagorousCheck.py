a=int(input("Enter the value of A\t"))
def pythagorous(a,b=5):
    #formula c^=a^*b^
    c=a**2*b**2
    return c
b=int(input("Enter the value of B\t"))
d=pythagorous(a,b)
print(d)