import sys 

def main():
    inputdata = sys.stdin.read().split()
    it = iter(inputdata)
    a = str(next(it))
    b = str(next(it))
    tab1 = [0 for _ in range(len(a))]
    counter1 = [0,0]
    for i in range(len(a)):
        if a[i] != b[i]:
            tab1[i] = 1
            if a[i] == '4':
                counter1[0] += 1
            else:
                counter1[1] += 1 
    ans1 = 0
    #print(counter1,counter2)
    def licz(ans,counter):
        while counter[0] > 0 and counter[1] > 0:
            ans+=1
            counter[0] -=1
            counter[1] -=1
        while counter[0] > 0:
            ans += 1
            counter[0] -= 1
        while counter[1] > 0:
            ans += 1
            counter[1] -= 1
        return ans
    ans1 = licz(0,counter1)

    print(ans1)

if __name__ == "__main__":
    main()