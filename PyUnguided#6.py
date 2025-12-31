#This project will be a turn base battle, there will be a player and an enemy. The enemy would be a bot that has RNG to make its decision
#It will ask the user what their role would be and what they would like to be called.
"""
game = input("Would you like to play a game? ").upper()

if game == "YES":
    role = input("Welcome, to a RNG turn base battle. Please select a role. (Archer/Barbarian/Wizard/Brute)").upper()
    if role == "ARCHER":
        print(f"You have chosen the class {role}")
    elif role == "BARBARIAN":
        print(f"You have chosen the class {role}")
    elif role == "WIZARD":
        print(f"You have chosen the class {role}")
    elif role == "BRUTE":
        print(f"You have chosen the class {role}")
    else:
        print("Invalid input, you lose.")

    def __init__(self, health, mana):
        self.health = health
        self.mana = mana
    """
class roles:
        
    def Archer(self):
        health = 100
        mana = 100
        self.health = health
        self.mana = mana
            
user_role = roles.Archer()


print(user_role)