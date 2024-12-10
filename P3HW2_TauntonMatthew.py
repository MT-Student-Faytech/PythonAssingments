# Matthew E. Taunton
# 12/5/2024
# P3HW2
# program calculates employee pay based on hours worked and wage

# Get employee's details
Name = input("Enter employee's name: ")
HoursWorked = float(input("Enter number of hours worked: "))
PayRate = float(input("Enter employee's pay rate: "))

# Print header
print('------------------------------------')
print(f'Employee name: {Name}')
print()

# Print table header
print(f'{"Hours Worked":<15}{"Pay Rate":<10}{"OverTime":<10}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<10}')
print('-' * 75)

# Calculate pay
if HoursWorked > 40:  # Handle overtime
    OverTime = HoursWorked - 40
    OverTimePay = OverTime * (PayRate * 1.5)
    RegHourPay = 40 * PayRate
else:  # No overtime
    OverTime = 0
    OverTimePay = 0
    RegHourPay = HoursWorked * PayRate

GrossPay = RegHourPay + OverTimePay

# Display results in formatted columns
print(f'{HoursWorked:<15.2f}{PayRate:<10.2f}{OverTime:<10.2f}{OverTimePay:<15.2f}{RegHourPay:<15.2f}{GrossPay:<10.2f}')

