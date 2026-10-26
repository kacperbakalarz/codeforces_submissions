import sys

def main():
    inputdata = sys.stdin.read().split()
    it = iter(inputdata)
    counter = int(next(it))
    for _ in range(counter):
        n = int(next(it))
        k = int(next(it))
        tab = [int(next(it)) for _ in range(n)]
        #tab = sorted(tab)[::-1]
        for i in range(len(tab)):
            rem = tab[i]%k
            if rem == 0:
                rem = k
            tab[i] = (rem,i+1)
        tab.sort(key=lambda x: (-x[0], x[1]))
        print(*(el[1] for el in tab))
    return 0
        
if __name__ == "__main__":
    main()
        


            