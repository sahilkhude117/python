my_list = [10,20,30]

try:
    # print("Value of x is:", x)

    print("Fourth element of list is: ", my_list[3])

    result = 100/0
    print("Result:", result)

except NameError as ne:
    print("Caught a NameError:", ne)

except IndexError as ie:
    print("Caught an IndexError:", ie)

except ZeroDivisionError as ze:
    print("Caught a ZeroDivisionError:",ze)

finally:
    print("Program execution completed.")