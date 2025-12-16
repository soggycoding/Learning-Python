name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You have came to the river, you can walk around it or swim accross? Type walk to walk around and Swim to swim accross: ").lower()
    if answer == "swim":
        print("You swam accross but got tangled through a vine and drowned, you lose")
    elif answer == "walk":
        answer = input("You found a bridge and tried to cross but while crossing the bridge broke, leaving you injured. Would you like to walk or take a rest ").lower()
        if answer == "walk":
            print("You walked for a little while but passed out through exhaustion........")
            answer = input("Luckily, you've rested without any interupptions and your injury have healed. Would you like to continue on your adventure or rest a little more? ").lower()
            if answer == "continue":
                print("You've continued and reached the village, Congratulations. You have won!")
            elif answer == "rest":
                print("You rested for a bit but a group of bears attacked you, you lose")
            else:
                print("You should have put a valid answer")
        elif answer == "rest":
            print("You are now resting, but while you were sleeping a bear attacked you, and sadly. You have died. You lose")
        else:
            print("Why didn't you put a valid answer. You lose")
    else:
        print('Not a valid option. You lose. ')
elif answer == "right":
    print("You were walking peacefully and saw a carrage on the way through the village, you've hitched hike and reached the village safetly. Congratulations, you have won!")
else:
    print('Not a valid option. You lose. ')
    
print("Thank you for trying", name)