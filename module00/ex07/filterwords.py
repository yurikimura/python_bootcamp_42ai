import sys

if len(sys.argv) == 3:
    text = sys.argv[1]
    try:
        num = int(sys.argv[2])
        wordlist = [word for word in text.split() if len(word) > num]
        print(wordlist)
    except:
        print("ERROR")
else:
    print("ERROR")
