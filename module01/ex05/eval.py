class Evaluator:
    def __init__(self):
        pass

    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        try:
            zipped = zip(coefs, words)
            s = 0
            for i in zipped:
                s += i[0] * len(i[1])
            return s
        except:
            return "TypeError"

    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        try:
            s = 0
            for i, c in enumerate(words):
                s += len(words[i]) * coefs[i]
            return s
        except:
            return "TypeError"
