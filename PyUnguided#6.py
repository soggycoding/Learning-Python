#This project will be a turn base battle, there will be a player and an enemy. The enemy would be a bot that has RNG to make its decision
#It will ask the user what their role would be and what they would like to be called.

game = input("Would you like to play a game? ").upper()

class roles:       
    def __init__(self,job, lvl, xp, hp, mana):
        self.job = job
        self.lvl = lvl
        self.xp = xp
        self.hp = hp
        self.mana = mana
        
    def __str__(self):
        return f"You have chosen {self.job} \nLEVEL:{self.lvl} \nXP:{self.xp}/100 \nHP:{self.hp} \nMANA:{self.mana}"
    
role1 = roles("ARCHER", 1, 0, 100, 100)
role2 = roles("BARBARIAN", 1, 0, 200, 100)
role3 = roles("WIZARD", 1, 0, 100, 300)
role4 = roles("BRUTE", 1, 0, 500, 50)

class skills:
    def __init__(self, s1, cost, dmg):
        self.s1 = s1
        self.cost = cost
        self.dmg = dmg
        
    def __str__(self):
        return f"The skill you have is called {self.s1} with the mana cost of {self.cost} and a dmg of {self.dmg}"
    """
    What to learn:
Instance methods - Methods that modify self attributes
Method parameters - Passing values (like mana cost) to methods
Basic arithmetic on attributes - self.mana -= cost
    """ 
    def use_skill(self, mana_cost):
        self.mana_cost -= mana_cost
        
skill1 = skills("Powershot", 50, 20)
skill2 = skills("Snipe", 100, 50)

if game == "YES":
    role = input("Welcome, to a RNG turn base battle. Please select a role. (Archer/Barbarian/Wizard/Brute)\n").upper()
    if role == "ARCHER":
        print(role1)
        skill = input("Would you like to see the skill of your chosen class? ").upper()
        if skill == "YES":
            print(skill1.s1)
    elif role == "BARBARIAN":
        print(role2)
    elif role == "WIZARD":
        print(role3)
    elif role == "BRUTE":
        print(role4)
    else:
        print("Invalid input, you lose.")
