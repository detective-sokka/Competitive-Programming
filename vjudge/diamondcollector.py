import sys

fin = open("diamond.in", "r")
fout = open("diamond.out", "w")

n, k = tuple(map(int, fin.readline().strip().split()))

diamonds = []

for _ in range(n):
    diamonds.append(int(fin.readline().strip()))

diamonds.sort()

best = [0 for _ in range(n)]
r = 0

for l in range(n):
    while (r < n and diamonds[r] - diamonds[l] <= k):
        r += 1
    best[l] = r - l

best_to_right = [-1 for _ in range(n+1)]

for i in range(n) [::-1]:
    best_to_right[i] = max(best_to_right[i+1], best[i])

ans = -1 

for l in range(n):
    ans = max(ans, best[l] + best_to_right[l + best[l]])

# print(ans)
fout.write(str(ans))