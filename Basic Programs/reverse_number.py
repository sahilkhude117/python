
number = int(input("Enter a number : "))
num1 = number

print("The reverse of number", num1, "is ", end='')
while num1 != 0:
    i = num1 % 10
    print(i, end='')
    num1 //= 10
while(num1 != 0):
    i = num1 % 10
    print(i, end='')
    num1 //= 10
