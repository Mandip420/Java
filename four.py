def grade_calculator():
    mark=float(input("Enter your marks\t"))
    if mark>=90 and mark<=100:
        return 'A grade'
    elif mark>=80 and mark<90:
        return 'B grade'
    elif mark>=70 and mark <90:
        return 'C grade'
    elif mark>=60 and mark <70:
        return 'D'
    elif mark>=50 and mark <60:
        return 'E'
    elif mark<50:
        return 'F'
    elif mark>100:
        print("Invalid mark")
        
d=grade_calculator()
print("Your grade is ",d)
if d=='F':
    print("You are fail")
  