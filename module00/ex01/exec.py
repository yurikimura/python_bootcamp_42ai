import sys

if len(sys.argv) == 2:
    text = sys.argv[1]
    print(text.swapcase()[::-1])

else:
    print("")
