# children = 0
# homeTown = "Raisio"

# # Lista
# TownsInFinland = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

# RandomInformation = ("Sami", 31, False, children, homeTown)

# print(TownsInFinland[0])
# TownsInFinland.append("Rovaniemi")
# print(TownsInFinland)

# NumberOfTowns = len(TownsInFinland)
# print(TownsInFinland [NumberOfTowns - 1])

# municaplities = ["Asikkala", "Holloha", "Karvia", "Kempele"]
towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

# MunicipalitiesAndTowns = [municaplities, towns]
# print(MunicipalitiesAndTowns[1][-2])

towns.sort()
# print(towns)

# teacher = {
#   'name': 'Juha',
#   'age': 50,
#   'city': 'Lahti'
# }
# print(teacher['name'])
# teacher['email'] = 'juha.hyytianen@lab.fi'
# print(teacher)

# for key in teacher:
#   print(key, end= ' ')
#   print(teacher[key])

# student = [
#   {'name': 'Sami', 'age': 31,'city': 'Raisio'},
#   {'name': 'Maija', 'age': 22,'city': 'Raisio'},
#   {'name': 'Seppo', 'age': 45,'city': 'Turku'}
# ]

# print(student[0])

# cities = {
#   'Finland':['Tampere', 'Espoo', 'Helsinki'],
#   'Sweden':['Stockholm', 'Malmö']
# }

# print(cities['Finland'][0])

# towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]
for town in towns:
  print(f"The town of {town}")
print(f"All the towns {towns}")

for i in range(1,10):
  print(i)

for i in range(1,10):
  print(i, end=' ')

print("")
for i in range(1,10, 3):
  print(i)

print(" ")
total = 0
for i in range(1,101):
  total +=i
  print(total)
print(total)

for i in range(9):
  if i == 3:
    continue
  print(i)

# Opiskele loopit for ja while, sekä niihin liittyvät komennot continiue ja break

i = 0
while i < 10:
  print(f"Interatio number {i}")
  i += 1

continueLoop = True
while continueLoop == True:
  if input("Do you want continiue? ") != "yes":
    continueLoop = False

while True:
  if input("Do you want continiue? ") != "yes":
    break
  else: 
    continue