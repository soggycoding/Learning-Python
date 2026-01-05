#This project will be a turn base battle, there will be a player and an enemy. The enemy would be a bot that has RNG to make its decision
#It will ask the user what their role would be and what they would like to be called.
import random
game = input("Would you like to play a game? ").upper()

player_roll = random.randint(1, 6)
enemy_roll = random.randint(1, 6)

        

class roles:       
    def __init__(self,job, lvl, xp, hp, mana):
        self.job = job
        self.lvl = lvl
        self.xp = xp
        self.hp = hp
        self.mana = mana
    
    def powershot(self):
        if self.mana >= 100:
            self.mana -= 30
            return "You have use Powershot! dealing 30 damage to the enemy"
    def snipe(self):
        if self.mana >= 100:
            self.mana -= 50
            return "You have use Snipe! dealing 50 damage to the enemy"
    def direct_shot(self):
        if self.mana >= 100:
            self.mana -= 60
            return "You have use Direct Shot! dealing 80 damage to the enemy"
    def multishot(self):
        if self.mana >= 100:
            self.mana -= 100
            return "You have use Multishot! dealing 100 damage to the enemy"    
    def __str__(self):
        return f"You have chosen {self.job} \nLEVEL:{self.lvl} \nXP:{self.xp}/100 \nHP:{self.hp} \nMANA:{self.mana}"
    
role1 = roles("ARCHER", 1, 0, 100, 100)
role2 = roles("BARBARIAN", 1, 0, 200, 100)
role3 = roles("WIZARD", 1, 0, 100, 300)
role4 = roles("BRUTE", 1, 0, 500, 50)

class enemy:
    def __init__(self,name, lvl, hp, mana):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.mana = mana
    def __str__(self):
        return f"{self.name} LEVEL:{self.lvl}, HP:{self.hp}, MANA:{self.mana}"
    
enemy1 = enemy("Dark Lord of Death", 50, 500, 1000)

"""
    What to learn:
Instance methods - Methods that modify self attributes
Method parameters - Passing values (like mana cost) to methods
Basic arithmetic on attributes - self.mana -= cost
"""

if game == "YES":
    role = input("Welcome, to a RNG turn base battle. Please select a role. (Archer/Barbarian/Wizard/Brute)\n").upper()
    if role == "ARCHER":
        print(role1)
        skill = input("Would you like to see the skill of your chosen class? ").upper()
        if skill == "YES":
            print("The Archer has these skills: \n1. Powershot \n2. Snipe \n3. Direct shot \n4. Multishot")
            start = input("Would you like to start the game? ").upper()
            if start == "YES":
                fight = input("You are walking along the forest and you have seen an enemy, are you going to fight it or run away? ").upper()
                if fight == "FIGHT":
                    die = input("This die will decide who will go first, input 1 to roll: ")
                    if die == "1":
                        print("You rolled: ", player_roll)
                        print(" ")
                        print("The enemy has rolled:", enemy_roll)
                        if player_roll > enemy_roll:
                            use_skill = input("Please select a number from the skills to attack the enemy: ")
                            if use_skill == "1":
                                print(roles.powershot(role1))
                            elif use_skill == "2":
                                print(roles.snipe(role1))
                            elif use_skill == "3":
                                print(roles.direct_shot(role1))
                            elif use_skill == "4":
                                print(roles.multishot(role1))
                            else:
                                print("Invalid input")
                        else:
                            print("The enemy goes first:")
    elif role == "BARBARIAN":
        print(role2)
    elif role == "WIZARD":
        print(role3)
    elif role == "BRUTE":
        print(role4)
    else:
        print("Invalid input, you lose.")
        
#This is a test
