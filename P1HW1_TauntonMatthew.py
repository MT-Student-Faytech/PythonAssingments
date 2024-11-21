#Matthew E. Taunton
#11/14/2024
#P1HW1
#write code that collects information from user, processes information collected and display results to user.

print('-----Calculating Exponenets-----')

print('\n')

base_value = float(input('Enter an integer as the base value: '))

exponent = float(input('Enter an interger as the exponent: '))

result = base_value ** exponent

print(f'{base_value} raised to the power of {exponent} is {result}')

print('\n')

print('-----Addition and Subtraction-----')

print('\n')

startingInteger = float(input('Enter a starting integer: '))

add = float(input('Enter an integer to add: '))

subtract = float(input('Enter an integer to subtract: '))

result1 = startingInteger + add - subtract

print(f'{startingInteger} + {add} - {subtract} is equal to {result1}')
