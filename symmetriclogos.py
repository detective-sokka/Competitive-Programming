# Symmetric logos - hackerearth (Accepted)

T = int(input())

for _ in range(T):
    no_flag = 0
    matrix = []
    N = int(input())
    for i in range(N):
        matrix.append(list(input()))
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '1':
                if matrix[N - i - 1][j] != '1' or matrix[i][N-j-1] != '1':
                    no_flag = 1
    if no_flag == 0:
        print("YES")
    else:
        print("NO")

