# https://www.codechef.com/problems/MRGSRT (Accepted)

'''
Testcase:
6
1 11 1
1 11 11
2 10 2
2 10 10
1 11 3
4 12 11


'''


def MergeSortCalc(s, t, i):
    mid = (s + t) // 2
    print("{} {}".format(s, t))
    if t == s == i:
        return 1

    if s <= i <= mid:
        return MergeSortCalc(s, mid, i) + 1
    elif mid < i <= t:
        return MergeSortCalc(mid + 1, t, i) + 1
    else:
        return -1


def main():
    T = int(input())
    s = 0
    t = 0
    i = 0
    for _ in range(T):
        (s, t, i) = map(int, input().split())
        print(MergeSortCalc(s, t, i))


if __name__ == "__main__":
    main()