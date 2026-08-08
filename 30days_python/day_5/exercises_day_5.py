lst = []
games = ['GTA VI', 'Bombanana', 'Rolbox', 'MLBB', 'LEAGUE']
print(len(games))
print(games[::2])
mixed_data_types = ['soggy', '21', '6.7', 'single', 'bahay namin']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[::3])
it_companies.pop(2)
print(it_companies)
it_companies.append("Anthropic")
print(it_companies)
it_companies.insert(4, "GMA")
print(it_companies)
upper = it_companies[6].upper()
it_companies.pop(6)
it_companies.insert(6, upper)
print(it_companies)
it_companies.extend("#")
print(it_companies)
company = "Google"
if company in it_companies:
    print("It is in")
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[3:9])
print(it_companies[0:6])
middle_index = len(it_companies) // 2
print(it_companies[middle_index:middle_index + 1]) # Slices out the middle company ['Facebook']
it_companies.remove("Oracle")
print(it_companies)
it_companies.remove("Facebook")
print(it_companies)
it_companies.remove("#")
print(it_companies)
it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

full_stack = front_end + back_end
print(full_stack)