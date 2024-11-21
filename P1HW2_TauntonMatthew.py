#Matthew E. Taunton
#11/14/2024
#P1HW2
#program that does some basic math on numbers that are entered.

print('This program calculates and displays travel expenses.')
print()
Budget = float(input('enter budget: '))
print()
destination = input('Enter your travel destination: ')
print()
gas = float(input('How much do you think youll spend on gas: '))
print()
accommodation = float(input('How much will you spend on accommodations: '))
print()
food = float(input('How much will you spend on food: '))

Total = Budget - gas - accommodation - food

print()
print('------------Travel Expenses------------')

print(f'Location: {destination}')
print(f'Initial Budget: {Budget}')
print()
print(f'Fuel: {gas}')
print(f'Accomodation: {accommodation}')
print(f'Food: {food}')
print()
print(f'Remaining Balance: {Total}')
