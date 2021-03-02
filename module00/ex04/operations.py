import sys

if len(sys.argv) == 1:
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
elif len(sys.argv) > 3:
    print("InputError: too many arguments\n\nUsage: python operations.py <number1> <number2>\
        \nExample:\n\tpython operations.py 10 3 ")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])

        if num2 == 0:
            Quotient = "ERROR (div by zero)"
            Remainder = "ERROR (modulo by zero)"
        else:
            Quotient = num1 / num2
            Remainder = num1 % num2

        print(f"Sum:          {num1+num2}")
        print(f"Difference:   {num1-num2}")
        print(f"Product:      {num1*num2}")
        print(f"Quotient:     {Quotient}")
        print(f"Remainder:    {Remainder}")

    except:
        print("InputError: only numbers\n\n\
        Usage: python operations.py < number1 > < number2 > \n\
        Example: \n\
        \tpython operations.py 10 3")

print("")
