#This project will be a turn base battle, there will be a player and an enemy. The enemy would be a bot that has RNG to make its decision
#It will ask the user what their role would be and what they would like to be called.
import random

player_roll = random.randint(1, 6)
enemy_roll = random.randint(1, 6)
enemy_attacks = random.randint(1, 5)

class roles:       
    def __init__(self,job, lvl, xp, hp, mana, skills):
        self.job = job
        self.lvl = lvl
        self.xp = xp
        self.hp = hp
        self.mana = mana
        self.skills = skills
    
    def powershot(self):
        if current_enemy.block_attack == True:
            current_enemy.block_attack = False
            return "The enemy has blocked your attack"
        elif self.mana > 0:
            current_player.mana -= 30
            current_enemy.hp -= 30
            return "You have use Powershot! dealing 30 damage to the enemy"
        return "Insufficient Mana, you have passed a turn"
    def snipe(self):
        if current_enemy.block_attack == True:
            current_enemy.block_attack = False
            return "The enemy has blocked your attack"
        elif self.mana > 0:
            current_player.mana -= 50
            current_enemy.hp -= 50
            return "You have use Snipe! dealing 50 damage to the enemy"
        return "Insufficient Mana, you have passed a turn"
    def direct_shot(self):
        if current_enemy.block_attack == True:
            current_enemy.block_attack = False
            return "The enemy has blocked your attack"
        elif self.mana > 0:
            current_player.mana -= 60
            current_enemy.hp -= 80
            return "You have use Direct Shot! dealing 80 damage to the enemy"
        return "Insufficient Mana, you have passed a turn"
    def multishot(self):
        if current_enemy.block_attack == True:
            current_enemy.block_attack = False
            return "The enemy has blocked your attack"
        elif self.mana > 0:
            current_player.mana -= 100
            current_enemy.hp -= 100
            return "You have use Multishot! dealing 100 damage to the enemy"
        return "Insufficient Mana, you have passed a turn"
    def user_block_attack(self):
        self.user_is_blocking = True
        return "You have blocked the enemy's attack!"
    def __str__(self):
        return f"________________________________________\nYou have chosen {self.job}: \nLEVEL:{self.lvl} \nXP:{self.xp}/100 \nHP:{self.hp} \nMANA:{self.mana} \n{self.skills}"
    
role1 = roles("ARCHER", 1, 0, 500, 500, "\n_________________SKILLS__________________ \n1: Powershot Damage: 30 Mana cost: 30 \n2: Snipe Damage: 50 Mana cost: 50 \n3: Direct Shot Damage: 80 Mana cost: 60 \n4: Multishot Damage: 100 Mana cost: 100\n5: Block\n________________________________________")
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
        if current_player.user_block_attack == True:
            current_player.user_block_attack = False
            return f"The {current_player} has blocked your attack"
        elif current_enemy.mana > 0:
            self.mana -= 50
            current_player.hp -= 30
            return "The enemy has used Swing! Dealing 30 damage to you"
        return "The enemy has no mana, and has pass to attack"
    
    def bane(self):
        if current_player.user_block_attack == True:
            current_player.user_block_attack = False
            return f"The {current_player} has blocked your attack"
        elif current_enemy.mana > 0:
            self.mana -= 100
            current_player.hp -= 50
            return "The enemy has used Bane! Dealing 50 damage to you"
        else:
            return "The enemy has no mana, and has pass to attack"
    
    def meditate(self):
        if self.mana != 0:
            self.mana -= 150
            current_enemy.hp + 100
            return f"The enemy has use Meditate, regenerating health by 100! His health is now {current_enemy.hp}"
        return "The enemy has no mana, and has pass to attack"
        
    def pass_attack(self):
        return "The enemy has pass to attack"
    
    def block_attack(self):
        self.is_blocking = True
        return "The enemy has use block!"
    
enemy1 = enemy("Dark Lord of Death", 50, 500, 1000)
current_player = role1
current_enemy = enemy1

archer_skills = {"1" : role1.powershot,
                 "2" : role1.snipe,
                 "3" : role1.direct_shot,
                 "4" : role1.multishot,
                 "5" : role1.user_block_attack}
enemy_skill = {1 : enemy1.swing,
               2 : enemy1.bane,
               3 : enemy1.meditate,
               4 : enemy1.pass_attack,
               5 : enemy1.block_attack}

class game_mechanics:
    def hp_update(self):
        if current_player.hp <= 0:
            print("You have died, game over!")
            exit()
        if current_enemy.hp <= 0:
            print("You have defeated the enemy, congratulations!")
            exit()
        if current_player.hp != 0:
            return f'Mana',current_player.mana,'HP',current_player.hp
        if current_enemy.hp != 0:
            return f'Mana:',current_enemy.mana,'HP:',current_enemy.hp
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
        print(archer_skills[user_input.skill_use()]())
        print("Enemy's Status: ",user_input.hp_update())
        game_design.divider()
        print("Enemy's turn")
        print(enemy_skill[enemy_attacks]())
        print("Your status: ",user_input.hp_update())
        game_design.divider()
    def enemy_first(self):
        print("It is the enemy's turn")
        print(enemy_skill[enemy_attacks]())
        print("Your status: ",user_input.hp_update())
        game_design.divider()
        print("It is now your turn, please choose a skill")
        print(archer_skills[user_input.skill_use()]())
        print("Enemy's Status: ",user_input.hp_update())
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
    current_player = role1
    print(current_player)
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
        while current_player.hp >= 0 or current_enemy.hp >= 0:
            user_input.user_first()
    else:
        print("The enemy is going first.")
        game_design.divider()
        while current_enemy.hp >= 0 or current_player.hp >= 0:
            user_input.enemy_first()

    """
    elif role == "BARBARIAN":
        print(role2)
    elif role == "WIZARD":
        print(role3)
    elif role == "BRUTE":
        print(role4)
    """