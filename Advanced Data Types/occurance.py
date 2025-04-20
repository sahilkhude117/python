my_list = [10,20,30,10,40,10,50,20,10]

search_value = int(input("Enter the value to search in the list: "))

count = 0
positions = []

for index, value in enumerate(my_list):
    if value == search_value:
        count += 1
        positions.append(index)
        
print(f"\nThe value {search_value} occurred {count} times.")
if count > 0:
    print("It was found at index positions:", positions)
else:
    print("The value was not found in the list.")