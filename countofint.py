# https://www.hackerearth.com/problem/algorithm/fact-count-a6300182/
# using segmented seive method

seive = []
primes = []


def generateSeive(input_max):
    global seive
    global primes
    seive = [True for i in range(input_max+1)]
    p = 2
    while p**2 <= input_max:
        if seive[p] is True:
            for j in range(p ** 2, input_max + 1, p):
                seive[j] = False
        p += 1
    seive[0] = False
    seive[1] = False
    for i in range(input_max):
        if seive[i] is True:
            primes.append(i)


generateSeive(100000)


def isPrime(input_num):
    global primes
    index = 0
    while primes[index] ** 2 <= input_num:
        if input_num % primes[index] == 0:
            return False
        index += 1
    return True


T = int(input())


for testcase in range(T):
    N = int(input())
    input_list = [int(x) for x in input().split()]
    result_count = 0
    for element in input_list:
        if isPrime(element):
            result_count += 1
    print(result_count)