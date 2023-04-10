# STPAR - spoj.com (Accepted)


def checkStackForMobiles(pStack, pExpected):
    while len(pStack) != 0 and pStack[-1] == pExpected:
        pExpected += 1
        pStack.pop()
    return pExpected


N = int(input())

while N != 0:
    stack_list = []
    expected_mobile = 1
    arrival_order = list(map(int, input().split()))
    for element in arrival_order:
        if element == expected_mobile:
            expected_mobile += 1
        else:
            expected_mobile = checkStackForMobiles(stack_list, expected_mobile)
            if element == expected_mobile:
                expected_mobile += 1
            else:
                stack_list.append(element)

    expected_mobile = checkStackForMobiles(stack_list, expected_mobile)

    if expected_mobile != N+1:
        print("no")
    else:
        print("yes")

    N = int(input())