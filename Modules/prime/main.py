import functions

def main():
    while True:
        print("\n===== MENU =====")
        print("1. Calculate Factorial")
        print("2. Check Prime Number")
        print("3. Calculate Power")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                num = int(input("Enter a number: "))
                print("Factorial: ", functions.factorial(num))

            elif choice == 2:
                num = int(input("Enter a number: "))
                if functions.primeNumber(num):
                    print(num, 'Is a prime number.')
                else: 
                    print(num, 'is NOT a Prime Number.')

            elif choice == 3:
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                print("Power: ", functions.powNumber(base, exponent))

            elif choice == 4:
                print("Exiting the program. Goodbye!")
                break

            else: 
                print("Invalid choice! Please select from 1 to 4.")

        except ValueError:
            print("Invalid input! Please enter numeric values only.")
        except Exception as e:
            print("An unexpected error occurred:", e)

main()
