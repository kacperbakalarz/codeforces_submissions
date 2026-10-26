import sys

def main(): 
    inputdata = sys.stdin.read().split()
    it = iter(inputdata)
    n = int(next(it))
    a = int(next(it))
    b = int(next(it))
    tab =[]
    c = str(next(it))
    #tab = [int(next(it)) for _ in range(n)]
    #print(tab[a-1],tab[b-1])
    if(c[a-1] == c[b-1]):
        print(0)
    else:
        print(1) 
    return 

if __name__ == "__main__":
    main()