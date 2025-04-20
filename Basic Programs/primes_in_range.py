start = int(input("Enter the starting number of the range: "))
end  = int(input("Enter the ending number of the range: "))

print(f'\n Prime numbers between {start} and {end} are: ')

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=' ')
