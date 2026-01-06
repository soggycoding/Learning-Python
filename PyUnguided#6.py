#This project will be a turn base battle, there will be a player and an enemy. The enemy would be a bot that has RNG to make its decision
#It will ask the user what their role would be and what they would like to be called.
import random

player_roll = random.randint(1, 6)
enemy_roll = random.randint(1, 6)
enemy_attacks = random.randint(1, 4)

class roles:       
    def __init__(self,job, lvl, xp, hp, mana, skills):
        self.job = job
        self.lvl = lvl
        self.xp = xp
        self.hp = hp
        self.mana = mana
        self.skills = skills
    
    def powershot(self):
        if self.mana >= 100:
            self.mana -= 30
            enemy1.hp -= 30
            return "You have use Powershot! dealing 30 damage to the enemy"
    def snipe(self):
        if self.mana >= 100:
            self.mana -= 50
            enemy1.hp -= 50
            return "You have use Snipe! dealing 50 damage to the enemy"
    def direct_shot(self):
        if self.mana >= 100:
            self.mana -= 60
            enemy1.hp -= 80
            return "You have use Direct Shot! dealing 80 damage to the enemy"
    def multishot(self):
        if self.mana >= 100:
            self.mana -= 100
            enemy1.hp -= 100
            return "You have use Multishot! dealing 100 damage to the enemy"    
    def __str__(self):
        return f"\n________________________________________You have chosen {self.job} \nLEVEL:{self.lvl} \nXP:{self.xp}/100 \nHP:{self.hp} \nMANA:{self.mana} \n{self.skills}"
    
role1 = roles("ARCHER", 1, 0, 100, 100, "\n_________________SKILLS__________________ \n1: Powershot Damage: 30 Mana cost: 30 \n2: Snipe Damage: 50 Mana cost: 50 \n3: Direct Shot Damage: 80 Mana cost: 60 \n4: Multishot Damage: 100 Mana cost: 100\n________________________________________")
"""
role2 = roles("BARBARIAN", 1, 0, 200, 100)
role3 = roles("WIZARD", 1, 0, 100, 300)
role4 = roles("BRUTE", 1, 0, 500, 50)
"""

class enemy:
    def __init__(self,name, lvl, hp, mana):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.mana = mana
    def __str__(self):
        return f"{self.name} LEVEL:{self.lvl}, HP:{self.hp}, MANA:{self.mana}"
    
    def swing(self):
        if self.mana >= 500:
            self.mana -= 50
            role1.hp -= 30
            return "The enemy has used Swing! Dealing 30 damage to you"
    
    def bane(self):
        if self.mana >= 500:
            self.mana -= 100
            role1.hp -= 50
            return "The enemy has used Bane! Dealing 50 damage to you"
    
    def meditate(self):
        if self.mana >= 500:
            self.mana -= 150
            role1.hp += 100
            return f"The enemy has use Meditate, regenerating health by 100! His health is now {enemy1.hp}"
        
    def pass_attack(self):
        return "The enemy has pass to attack"
    
enemy1 = enemy("Dark Lord of Death", 50, 500, 1000)
player_hp = role1.hp
enemy_hp = enemy1.hp

archer_skills = {"1" : role1.powershot,
                 "2" : role1.snipe,
                 "3" : role1.direct_shot,
                 "4" : role1.multishot}
enemy_skill = {1 : enemy1.swing,
               2 : enemy1.bane,
               3 : enemy1.meditate,
               4 : enemy1.pass_attack}

class game_mechanics:
    def skill_use(self):
        self.use_skill = input("Please select a number from the skills to attack the enemy: ")
        return self.use_skill
    def start_game(self):
        self.start = input("Would you like to start the game? ").upper()
        return self.start
    def fight(self):
        self.fight_enemy = input("Would you like to fight an enemy? ").upper()
        return self.fight_enemy
    def user_role(self):
        self.role = input("Welcome, to a RNG turn base battle. Please select a role. (Archer/Barbarian/Wizard/Brute)\n").upper()
        return self.role
    def game_start(self):
        self.game = input("Would you like to play a game? ").upper()
        return self.game
    def user_first(self):
        print("It is now your turn")
        while role1.hp > 0 and enemy1.hp > 0:
            print(archer_skills[user_input.skill_use()]())
            game_design.divider()
            print("Enemy's turn")
            print(enemy_skill[enemy_attacks]())
            game_design.divider()
    def enemy_first(self):
        print("It is the enemy's turn")
        while role1.hp > 0 and enemy1.hp > 0:
            print(enemy_skill[enemy_attacks]())
            game_design.divider()
            print("It is now your turn, please choose a skill")
            print(archer_skills[user_input.skill_use()]())
            game_design.divider()
            
class design:
    def divider(self):
        print("________________________")
            
game_design = design()

user_input = game_mechanics()

if user_input.game_start() != "YES":
    print("Invalid input, you lose.")
    exit()
if user_input.user_role() == "ARCHER":
    print(role1)
    if user_input.start_game() != "YES":
        print("Game over!")
        exit()
    if user_input.fight() != "YES":
        print("You have chosen to run away, coward")
        exit()
    game_design.divider()
    print("You rolled: ", player_roll)
    print("The enemy has rolled:", enemy_roll)
    game_design.divider()
    if player_roll > enemy_roll:
        print("You are going first.")
        game_design.divider()
        user_input.user_first() 
    else:
        print("The enemy is going first.")
        game_design.divider()
        user_input.enemy_first()
    """
    elif role == "BARBARIAN":
        print(role2)
    elif role == "WIZARD":
        print(role3)
    elif role == "BRUTE":
        print(role4)
    """