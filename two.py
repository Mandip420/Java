class character:
    def __init__(self,choose_character):
     self.choose_character=choose_character
     
    def get_power(self):
        self.choose_character=input("Choose the character\t  warroir , Mega , Roque\t")
        if self.choose_character=="warrior":
            print("The attack power of warrior is  10")
        
        elif self.choose_character=="mega":
             print("The attack power of warrior is  8")
             
        elif self.choose_character=="roque":
            print("The attack power of warrior is  6")
            
        else:
            print("Please choose a valid character")
        
if __name__ == "__main__":  
    player=character(choose_character=None)
    player.get_power()