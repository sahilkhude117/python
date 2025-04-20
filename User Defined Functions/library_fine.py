from datetime import datetime

def calculate_fine(return_date_str, due_date_str, condition):
    return_date = datetime.strptime(return_date_str, "%d-%m-%Y")
    due_date = datetime.strptime(due_date_str, "%d-%m-%Y")

    fine = 0

    if return_date > due_date:
        days_late = (return_date - due_date).days
        fine += days_late * 2

    if condition.lower() == 'damaged':
        fine += 50

    elif condition.lower() == 'lost':
        fine += 200

    return fine

return_date = input("Enter return date (dd-mm-yyyy): ")
due_date = input("Enter due date (dd-mm-yyyy): ")
condition = input("Enter book condition (Good/Damaged/Lost): ")

total_fine = calculate_fine(return_date, due_date, condition)

print("Total Library Fine: Rs.", total_fine)