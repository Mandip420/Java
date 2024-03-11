#Check wheather given number is odd or not:
def odd():
    if a%2==0:
        return False
    else:
        return True
a=int(input("Enter the value of A\t"))
d=odd()

if odd() is False:
   print(d , "It is even")
# elif d is True:
elif odd() is True:
    print(d, "It is odd")