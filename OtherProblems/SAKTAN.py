# codechef problem code - SAKTAN

T = int(input())
for _ in range(T):
    count=0
    N = int(input())
    prices = [int(x) for x in input().split()]
    for i in range(len(prices)):
        temp = i
        for j in range(5):
            temp -= 1
            if temp < 0:
                break
            if(prices[i] >= prices[temp]):
                count -= 1
                break
        count += 1
    print(count)