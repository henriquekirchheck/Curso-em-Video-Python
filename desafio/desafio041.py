from datetime import date

year = date.today().year

age = int(input('Digite seu ano de nascimento: '))
age = year - age

if(age <= 9):
    print('Mirim')
elif((age > 9) and (age <= 14)):
    print('Infantil')
elif((age > 14) and (age <= 19)):
    print('Junior')
elif((age > 19) and (age <= 20)):
    print('Sênior')
else:
    print('Master')
