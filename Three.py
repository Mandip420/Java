def check_eligibility(age):      
    if(age>=18):
         return True
    else:
        return False
age=int(input("Enter age for checking eligibility\t"))   
d=check_eligibility(age)
if d==True:
    print(d, "You are eligible for registration ")
else:
    print(d, "You are not eligible for registration ")
    