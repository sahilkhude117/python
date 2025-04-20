my_list = [45, 12, 78, 34, 89, 23, 67]

print("Original List: ", my_list)

choice = int(input("Press 1 for Ascending Order or Press 2 for Descending Order: "))

n = len(my_list)

if choice == 1:
    for i in range(n):
        for j in range(0, n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

    print("List in Ascending Order:", my_list)

elif choice == 2:
    for i in range(n):
        for j in range(0, n-i-1):
            if my_list[j] < my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    
    print("List in Ascending Order:", my_list)

else:
    print("Invalid choice. Please enter 1 or 2 only.")
        