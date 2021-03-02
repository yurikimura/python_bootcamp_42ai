import time
import sys


def ft_progress(charge: range):
    try:
        start = time.time()
        length = len(str(max(charge)))
        eta = 0
        barsize = 50
        for i in charge:
            per = i/max(charge)*100
            bar = int(i/max(charge)*barsize)
            t = time.time() - start
            if per > 0:
                eta = t/per*100
            sys.stdout.write('\r')
            sys.stdout.write("ETA: %.2fs [%3d%%] [%-*.*s] %*d/%d | elapsed time %.2fs" %
                             (eta, per, barsize, barsize, '='*bar+'>', length, i, max(charge), t))
            yield i
    except:
        print("ERROR: parameter must be range object")


def main():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)


if __name__ == "__main__":
    main()
