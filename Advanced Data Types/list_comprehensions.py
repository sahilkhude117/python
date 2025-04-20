

end = int(input("Enter number to find squares till that number: "))

squares = [x**2 for x in range(1, end + 1)]

print("Squares from 1 to 10:", squares)


numbers = [1, 4, 7, 10, 15, 18, 21, 24]

even_numbers = [num for num in numbers if num % 2 == 0]

print("Even numbers from the list:", even_numbers)

