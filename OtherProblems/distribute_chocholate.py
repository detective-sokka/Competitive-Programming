# https://www.hackerearth.com/challenges/competitive/january-circuits-20/algorithm/distribute-chocolates-70c2c2ab/
# Accepted

def CalculateRemainingChocholate(c, n):
    k_val = (c - (n * (n + 1) // 2)) // n
    if k_val < 0:
        return c
    min_choc = n * k_val + (n * (n + 1) // 2)
    return c - min_choc


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        c, n = map(int, input().split())
        print(CalculateRemainingChocholate(c, n))
