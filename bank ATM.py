class bank_ATM:
    def __init__(self) -> None:
        self.balance=0
        
        
    def deposit(self):
        amount=float(input("Enter the deposit amount\t"))
        if amount  >  0:
            print("Deposit successfull\t")
            self.balance+=amount
        else:
            print("Amount most should be greater than  '0'")
        p.menu()
        
    
    def widral(self):
        amount=float(input("Enter the widral amount\t"))
        if self.balance > amount:
            print("Widral successfull")
            self.balance-=amount
        else:
            print("Sorry insufficient balance")
        p.menu()
        
    def check_balance(self):
        print("The available balance is ",self.balance)
        p.menu()
        
        
    def menu(self):
        print("1.Deposit amount\t\t\t\t2.Widral amount")
        print()
        print("3.check balance\t\t\t\t4.Return")
        choice=int(input("Enter your choice\t"))
        
        if choice==1:
            p.deposit()
            
        elif choice==2:
            p.widral()
            
        elif choice==3:
            p.check_balance()
            
        elif choice==4:
            return
        
    def check_pin(self):
        pin=1200
        entered_pin=int(input("Enter your pin"))
        if pin==entered_pin:
            p.menu()
            
        else:
            print("Incorrect pin")
            print()
            print("please enter a valid pin")
            
if __name__ == "__main__":
    p = bank_ATM()
    p.check_pin()