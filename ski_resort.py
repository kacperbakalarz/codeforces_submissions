import sys

def main():
    inputdata = sys.stdin.read().split()
    it = iter(inputdata)
    counter = int(next(it))
    for _ in range(counter):
        n = int(next(it))
        k = int(next(it))
        q = int(next(it))
        curr = 0
        row = [int(next(it)) for _ in range(n)]
        ans = 0
        for el in row:
            if el <= q:
                curr+=1
                if curr >= k:
                    ans += curr-k+1
            else:
                curr = 0
        print(ans)

if __name__ == "__main__":
    main()

                

            


    