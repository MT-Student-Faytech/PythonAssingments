# Matthew E. Taunton
# 11/26/2024
# P2LAB2
# A program that creates a dictionary where the keys and values are paired.

Cars = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model_S': 110.0,
    'Silverado': 26.0
}

keys = Cars.keys()

print(keys)
print()
car_model = input("Enter a vehicle to see it's mpg: ")
print()
if car_model in Cars:
    print(f"the {car_model} gets {Cars[car_model]:.2f}mpg.")
else:
    print('Not an entry')
print()
miles = float(input(f'How many miles will you drive the {car_model}? '))
print()
mpg = Cars[car_model]
gallons = miles / mpg

print(f'{gallons:.2f} gallon(s) of gas are needed to drive the {car_model} {miles} miles.')
