# Matthew E. Taunton
# 12/5/2024
# P3HW2
# program calculates employee pay based on hours worked and wage

# Initialize counters for totals
total_employees = 0
total_amount_paid_overtime = 0.0
total_paid_reg = 0.0
total_paid_gross = 0.0

# Loop to get employee details
while True:
    # Get employee details
    print()
    Name = input("Enter employee's name or 'done' to terminate: ")
    if Name.lower() == 'done':  # Check if user wants to terminate
        break

    try:
        HoursWorked = float(input("Enter number of hours worked: "))
        PayRate = float(input("Enter employee's pay rate: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for hours worked and pay rate.")
        continue

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

    # Update totals
    total_employees += 1
    total_amount_paid_overtime += OverTimePay
    total_paid_reg += RegHourPay
    total_paid_gross += GrossPay

    # Print header and table row
    print('------------------------------------')
    print(f'Employee name: {Name}')
    print()
    print(f'{"Hours Worked":<15}{"Pay Rate":<10}{"OverTime":<10}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<10}')
    print('-' * 75)
    print(f'{HoursWorked:<15.2f}{PayRate:<10.2f}{OverTime:<10.2f}{OverTimePay:<15.2f}{RegHourPay:<15.2f}{GrossPay:<10.2f}')

# Print final totals
print('\n------------------------------------')
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_amount_paid_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_paid_reg:.2f}")
print(f"Total amount paid in gross: ${total_paid_gross:.2f}")
