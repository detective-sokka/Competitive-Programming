# https://www.codechef.com/problems/TACHSTCK (Accepted)
'''
test case:
5 2
1
3
3
9
4
'''

def main():
    N, D = map(int, input().split())
    i = 0
    list_ = []
    while i < N:
        list_.append(int(input()))
        i += 1

    list_.sort()
    i = 1
    count = 0
    while i < N:
        if list_[i] - list_[i-1] <= D:
            i += 1
            count += 1

        i += 1
    print(count)


if __name__ == "__main__":
    main()