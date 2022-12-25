# Intro to memoization with Fibonacci series problem


def printFibonacci(input_num):
    if input_num == 1:
        print("0")
        return
    memo = [0] * (input_num+1)
    memo[1] = 0
    memo[2] = 1
    if input_num == 2:
        print(memo)
        return
    for index in range(3, input_num+1):
        memo[index] = memo[index-1] + memo[index-2]
    memo.pop(0)
    print(memo)


def FibonacciIterative(input_num):
    if input_num == 0:
        print("0")
        return

    elif input_num == 1:
        print("0 1", end=" ")
        return
    old = 0
    new = 1

    print("0 1", end=" ")

    for i in range(input_num - 2):
        (old, new) = (new, old + new)
        print(new, end=" ")

    return new


N = int(input())
printFibonacci(N)
print(FibonacciIterative(N))