import sys

def main():
    inputdata = sys.stdin.read().split()
    it = iter(inputdata)
    first= str(next(it))
    last = str(next(it))
    login1 = first[0]
    i = 1
    while i < len(first):
        if first[i] < last[0]:
            login1 += first[i]
            i += 1
        else:
            break
    login1 += last[0]
    print(login1)
        
if __name__ == "__main__":
    main()
        


            