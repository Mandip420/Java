def odd(a=50):
    odds=[]
    for i in range(1,a,1):
        if (i%2!=0):
            odds.append(i)
    return odds
b=int(input("Enter the range\t"))     
d=odd(b)
print(d)