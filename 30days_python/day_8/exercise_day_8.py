# Exercise: Day 8

dog = {}
dog = {
    'name' : '',
    'color' : '',
    'age' : 0,
    'breed' : '',
    'legs' : ''
}

student = {
    'first_name' : '',
    'last_name' : '',
    'gender' : 'Male',
    'age' : 0,
    'marital_status' : '',
    'skills' : '',
    'country' : '',
    'city' : '',
    'address' : ''
}

print(len(student))
print(student['skills'])
student['skills'] = ['HTML', 'CSS', 'JavaScript', 'Python']
print(type(student['skills']))
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
student.pop("gender")
print(student)
student.clear()
del dog