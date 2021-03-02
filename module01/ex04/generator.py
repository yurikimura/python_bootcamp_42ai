# forbitten function: random.shuffle
from random import randint


def generator(text, sep=" ", option=None):
    try:
        words = text.split()
        if option == "shuffle":
            id_list = [i for i in range(len(words))]
            while id_list != []:
                idx = randint(0, len(id_list)-1)
                print(words[id_list[idx]])
                id_list.remove(id_list[idx])

        elif option == "ordered":
            for i in sorted(words, key=str.lower):
                print(i)

        elif option == "unique":
            for i in set(words):
                print(i)

        elif option == None:
            for i in words:
                print(i)

        else:
            print("ERROR")
    except:
        print("ERROR")


text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
    print(word)
