# Matthew E. Taunton
# 11/26/2024
# P2HW2
# A program that creates a dictionary where the key and value are paired.

G1 = float(input('Enter grade for Module 1: '))
G2 = float(input('Enter grade for Module 2: '))
G3 = float(input('Enter grade for Module 3: '))
G4 = float(input('Enter grade for Module 4: '))
G5 = float(input('Enter grade for Module 5: '))
G6 = float(input('Enter grade for Module 6: '))

grades = [G1, G2, G3, G4, G5, G6]

low = min(grades)
high = max(grades)
sumG = sum(grades)
avg = sum(grades)/ len(grades)

print('\n------------Results------------')
print(f'Lowest Grade:    {low:.1f}')
print(f'Highest Grade:   {high:.1f}')
print(f'Sum of Grades:   {sumG:.1f}')
print(f'Average:         {avg:.2f}')
print('----------------------------------')


