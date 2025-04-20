def modify_list(input_list):
    new_list = []
    for element in input_list:
        new_list.append(element * 2)
    return new_list

original_list = []

n = int(input("Enter number of elements in the list: "))
for i in range(n):
    val = int(input(f'Enter element {i+1}: '))
    original_list.append(val)

modified = modify_list(original_list)

print("Original List: ", original_list)
print("Modified List (Elements Doubled):", modified)