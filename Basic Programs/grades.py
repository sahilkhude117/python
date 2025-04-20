marks = []

for i in range(1, 6):
    mark = float(input(f'Enter marks of subject { i }: '))
    marks.append(mark)

total = 0 

for i in marks:
    total = total + i
    
average = total / 5

if average >= 90:
    grade = 'A+'
elif average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B+'
elif average >= 60:
    grade = 'B'
elif average >= 50:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'F'

print(f"\nTotal Marks: {total}/500")
print(f"Average Marks: {average}")
print(f"Grade: {grade}")