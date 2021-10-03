print('Choose a number between 1 and 10')

myInt = input()

calc_1 = ((int(myInt) * 2) + 5) * 50
myNumber = calc_1

print('Have you celebrated your birthday this year yet?')

myAnswer = input()

if myAnswer == 'yes':
    calc_2 = myNumber + 1771

if myAnswer == 'no':
    calc_2 = myNumber + 1770

print('What year were you born in?')
birth_year = input()

output = int(calc_2 - int(birth_year))
print(output)
print('The First number is the number you chose and the other 2 digits are your age')