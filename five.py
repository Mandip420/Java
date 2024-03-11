class Voter:
    def __init__(self,age) -> None:
        self.age=age
    def can_vote(self):
        if self.age>=16:
            return True
        elif self.age<16:
            return False
        else:
            return "Wrong input"
age=int(input("enter you age\t"))
a=Voter(age)
a.can_vote()
if a.can_vote()==True:
    print(a.can_vote())
    print("You are eligible for voting")
else:
    print(a.can_vote())
    print("You can't vote you are not eligible for voting")
    

