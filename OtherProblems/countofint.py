# https://www.hackerearth.com/problem/algorithm/fact-count-a6300182/
import numpy as np
max_sieve = 100000000
sieve_array = np.ones(max_sieve+1, dtype=bool)
sieve_array[0] = False
sieve_array[1] = False


def generateSieve():
    index = 2
    while index * index <= max_sieve:
        if sieve_array[index]:
            sieve_array[index*index::index] = False

        index += 1


T = int(input())
generateSieve()

for _ in range(T):
    N = int(input())
    testcase_input = list(map(int, input().split()))
    testcase_count = 0

    for element in testcase_input:
        if sieve_array[element]:
            testcase_count += 1

    print(testcase_count)