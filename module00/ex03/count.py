def text_analyzer(*args):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""

    if len(args) > 1:
        print("ERROR")
        return

    elif len(args) == 0:
        print("What is the text to analyse?")
        text = input()

    else:
        text = args[0]

    upper_count = 0
    lower_count = 0
    punc_marks = 0
    spaces = 0
    punc = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    for i in text:
        if i.isupper():
            upper_count += 1
        if i.islower():
            lower_count += 1
        if i == " ":
            spaces += 1
        if i in punc:
            punc_marks += 1

    print(f"The text contains {len(text)} characters")
    print(f"- {upper_count} upper letters")
    print(f"- {lower_count} lower letters")
    print(f"- {punc_marks} punctuation marks")
    print(f"- {spaces} spaces")

    return
