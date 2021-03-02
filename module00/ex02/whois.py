import sys

if len(sys.argv) == 1:
    pass
elif len(sys.argv) != 2:
    print("ERROR")
else:
    arg = sys.argv[1]
    try:
        num = int(arg)
        if num == 0:
            print("I'm Zero.")
        elif num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except:
        print("ERROR")
