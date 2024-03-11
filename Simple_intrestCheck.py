P=float(input("Enter the Principal\n"))
def simple_intrest(P,T,R):
    SI=(P*T*R)/100
    return SI
T=float(input("Enter the time period\n"))
d=simple_intrest(P,T,R=1000)
print("The simple intrest =\t",d)