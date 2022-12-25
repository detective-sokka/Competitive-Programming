# codechef code - S10E
"""
1
13
1 1 1 1 1 2 3 3 3 4 1 4 5
"""


def checkMinimum(test_elem, vQueue):
    for iterator in vQueue:
        if iterator <= test_elem:
            return False
    return True


T = int(input())
aQ = []

for i in range(T):
    N = int(input())
    count_result = 0
    str_list = input().split(' ')
    aQ = []
    for element in str_list:
        element = int(element)
        if len(aQ) == 6:
            aQ.pop(0)
        if checkMinimum(element, aQ):
            count_result += 1
        aQ.append(element)
    print(count_result)
