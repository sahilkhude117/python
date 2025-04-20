def calculate_net_salary(emp_type, monthly_salary=0, hourly_rate=0, present_days=0, 
                         bonus=0, income_tax=0):
    total_days = 30
    working_hours_per_day = 8
    
    if emp_type.lower() == "permanent":
        per_day_salary = monthly_salary / total_days
        gross_salary = per_day_salary * present_days + bonus
    elif emp_type.lower() == "temporary":
        gross_salary = hourly_rate * working_hours_per_day * present_days + bonus
    else:
        print("Invalid employee type.")
        return 0
    
    net_salary = gross_salary - income_tax
    return net_salary

emp_type = input("Enter employee type (Permanent/Temporary): ").strip()

if emp_type.lower() == "permanent":
    monthly_salary = float(input("Enter monthly salary: "))
    present_days = int(input("Enter number of present days (out of 30): "))
    bonus = float(input("Enter incentives/bonus (if any): "))
    income_tax = float(input("Enter income tax amount: "))
    net = calculate_net_salary(emp_type, monthly_salary=monthly_salary,
                                present_days=present_days,
                                bonus=bonus, income_tax=income_tax)
    
elif emp_type.lower() == "temporary":
    hourly_rate = float(input("Enter hourly rate: "))
    present_days = int(input("Enter number of present days: "))
    bonus = float(input("Enter incentives/bonus (if any): "))
    income_tax = float(input("Enter income tax amount: "))
    net = calculate_net_salary(emp_type, hourly_rate=hourly_rate,
                                present_days=present_days,
                                bonus=bonus, income_tax=income_tax)
else:
    net = 0

print("\n🧾 Net Monthly Salary: Rs.", net)
