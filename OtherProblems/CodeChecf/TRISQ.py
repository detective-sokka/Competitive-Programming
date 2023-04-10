# https://www.codechef.com/problems/TRISQ (Accepted)


def computeSquares(num):
    total_squares = 0
    n = num
    while n > 3:
        total_squares = total_squares + 1 + 2 * ((n-4)//2)
        n = n - 4
    return total_squares


T = int(input())
for _ in range(T):
    N = int(input())
    print(computeSquares(N))

