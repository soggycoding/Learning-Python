# Exercise Day 10:
'''
for i in range(0,11):
    print(i)
'''
'''
for i in range(11,0,-1):
    print(i)
'''
'''
for i in range(1,8):
    if i == 1:
        print("*")
    elif i == 2:
        print("**")
    elif i == 3:
        print("***")
    elif i == 4:
        print("****")
    elif i == 5:
        print("*****")
    elif i == 6:
        print("******")
    elif i == 7:
        print("*******")
'''
'''
num = 0
while num != 7:
    for i in range(1,8):
        print(" #", end= " ")
        if i == 7:
            print("")
            num = num + 1
'''
'''
num = 0
for mult in range(0,11):
    answer = num * mult
    print(num , " x " , mult ," = ", answer)
    num = num + 1
'''
'''
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)
'''
'''
for even in range(0,101):
    if even % 2:
        pass
    else:
        print(even)
'''
'''
for odds in range(0,101):
    if odds % 2:
        print(odds)
    else:
        pass
'''
'''
number = 0
for nums in range(0,101):
    new_nums = nums + number
    number = number + nums
    print(new_nums)
'''
number = 0
even = 0
odds = 0
for nums in range(0,101):
    new_nums = nums + number
    number = number + nums
    if new_nums % 2:
        odds = new_nums
    elif new_nums % 3:
        even = new_nums
    else:
        pass
print("The sum of all evens are: ", even)
print("The sum of all odds are: ", odds)