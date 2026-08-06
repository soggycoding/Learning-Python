# Exercise Day: 9

## Exercise Level 1:
age = input("Enter your age: ")
age = int(age)
if age >= 18:
    print("You are old enough to learn to drive. ")
elif age < 18:
    print("Wait for at least " + str(18 - age) + " years to learn to drive.")
else:
    print("Invalid input")

my_age = input("Input my age: ")
your_age = input("Input your age: ")
my_age = int(my_age)
your_age = int(your_age)

if my_age > your_age:
    print("I am older than you by " + str(my_age - your_age) + " years.")
elif my_age < your_age:
    print("You are older than me by " + str(your_age - my_age) + " years.")
else:
    print("We are the same age. ")

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

student_score = ("Please input your score to see your grades: ")
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