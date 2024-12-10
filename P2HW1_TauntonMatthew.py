#Matthew E. Taunton
#11/14/2024
#P2HW1
#program that does some basic math on numbers that are entered.

print('This program calculates and displays travel expenses.')
print()
Budget = float(input('enter budget: '))
print()
destination = input('Enter your travel destination: ')
print()
gas = float(input('How much do you think youll spend on gas? '))
print()
accommodation = float(input('How much will you spend on accommodations? '))
print()
food = float(input('How much will you spend on food? '))

Total = Budget - gas - accommodation - food

print()
print('------------Travel Expenses------------')

print(f'Location:          {destination}')
print(f'Initial Budget:    ${Budget:,.2f}')
print(f'Fuel:              ${gas:,.2f}')
print(f'Accomodation:      ${accommodation:,.2f}')
print(f'Food:              ${food:,.2f}')
print('---------------------------------------')
print()
print(f'Remaining Balance: ${Total:,.2f}')
