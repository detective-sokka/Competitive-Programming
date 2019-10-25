# codechef code - RAINBOWA

"""
5
20
1 2 3 4 4 5 6 6 7 7 7 7 6 6 5 4 4 3 2 1
17
1 1 1 2 3 4 5 6 7 6 5 4 3 2 1 1 1
15
1 2 2 4 4 5 6 7 6 5 4 4 2 2 1
20
2 2 3 4 4 5 6 6 7 7 7 7 6 6 5 4 4 3 2 2
15
1 1 2 4 4 5 6 7 6 5 4 4 2 2 1

Answers:
Yes
Yes
No
No
No

"""

T = int(input())


def searchZero(a_list):
    for element in a_list:
        if element == 0:
            return True
    return False


for i in range(T):
    N = int(input())
    if N < 13:
        print("no")
        continue
    input_list = [int(x) for x in input().split()]
    index = int(N / 2)
    if input_list[index] != 7:
        print("no")
        continue
    is_present = [0, 0, 0, 0, 0, 0, 0]
    is_present[6] = 1
    no_flag = 0
    index = index - 1
    while index >= 0:
        if input_list[index] != input_list[N - index-1]:
            no_flag = 1
            break
        elif input_list[index] < 1 or input_list[index] > 7:
            no_flag = 1
            break
        is_present[input_list[index]-1] = 1
        if input_list[index] != 7 and is_present[input_list[index]] == 0:
            no_flag = 1
            break
        index -= 1

    if no_flag == 1 or searchZero(is_present):
        print("no")
    else:
        print("yes")
