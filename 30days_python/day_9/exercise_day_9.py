# Exercise Day: 9
'''
## Exercise Level 1:
age = input("Enter your age: ")
age = int(age)
if age >= 18:
    print("You are old enough to learn to drive. ")
elif age < 18:
    print("Wait for at least " + str(18 - age) + " years to learn to drive.")
else:
    print("Invalid input")
'''
my_age = input("Input my age: ")
your_age = input("Input your age: ")
my_age = int(my_age)
your_age = int(your_age)
age_gap = abs(my_age - your_age)

if age_gap > 1:
    if my_age > your_age:
        print("I am older than you by " + str(age_gap) + " years.")
    else:
        print("You are older than me by " + str(age_gap) + " years.")
elif age_gap == 1:
    if my_age > your_age:
        print("I am older than you by " + str(age_gap) + " year.")
    else:
        print("You are older than me by " + str(age_gap) + " year.")
else:
    print("We are the same age. ")
'''
a = input("Assign the number for a: ")
a = int(a)
b = input("Assign the number for b: ")
b = int(b)

if a > b:
    print(str(a) + " is greater than " + str(b))
elif a < b:
    print(str(a) + " is less than " + str(b))
else:
    print(str(a) + " is equal to " + str(b))

## Exercise Level 2: 

student_score = input("Please input your score to see your grades: ")
student_score = int(student_score)
if student_score >= 90:
    print("Your grade is A")
elif student_score >= 80:
    print("Your grade is B")
elif student_score >= 70:
    print("Your grade is C")
elif student_score >= 60:
    print("Your grade is D")
elif student_score < 60:
    print("Your grade is F")
else:
    print("Invalid input, try again")

get_month = input("Enter a month: ")
get_month = get_month.upper()
if get_month == "SEPTEMBER" or get_month == "OCTOBER" or get_month == "NOVEMBER":
    print("The season is Autumn.")
elif get_month == "DECEMBER" or get_month == "JANUARY" or get_month == "FEBRUARY":
    print("The season is Winter.")
elif get_month == "MARCH" or get_month == "APRIL" or get_month == "MAY":
    print("The season is Spring.")
elif get_month == "JUNE" or get_month == "JULY" or get_month == "AUGUST":
    print("The season is Summer.")
else:
    print("Invalid input, try again")

fruits = ['banana', 'orange', 'mango', 'lemon']
input_fruit = input("Please input a fruit: ")
if input_fruit in fruits:
    print("It is already in the list")
else:
    fruits.append(input_fruit)
    print("Added to the list. " + str(fruits))

# Exercise Level 3:
person_a = {'name': 'John', 
            'age': 30
            , 'skills': ['Python', 'MongoDB', 'Node', 'React'],
            'married' : True,
            'country' : 'Tondo'}

if person_a['skills']:
    middle_index = len(person_a['skills']) // 2
    print(person_a['skills'][middle_index])
    if 'Python' in person_a['skills']:
        print("He also have skills in Python") 
if 'Javascript' in person_a['skills'] and 'React' in person_a['skills']:
    print("He is a front end developer")
elif 'Node' in person_a['skills'] and 'Python' in person_a['skills'] and 'MongoDB' in person_a['skills']:
    print("He is a backend developer")
elif 'React' in person_a['skills'] and 'Node' in person_a['skills'] and 'MongoDB' in person_a['skills']:
    print('He is a fullstack developer')
else:
    print('Unknown Title. ')

if person_a['married'] == True and person_a['country'] == 'Tondo':
    print(person_a['name'] + ' is from ' + person_a['country'] + ' and is married.')
else:
    print('debug time')
'''