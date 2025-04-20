list1 = [10, 20, 30]
list2 = [40, 50, 60]

print("List1 before adding:", list1)
print("List2:", list2)

for element in list2:
    list1.append(element)

print("Updated List1 after adding List2 elemets: ", list1)