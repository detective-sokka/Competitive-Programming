# https://www.codechef.com/problems/LFSTACK (Accepted)

'''
Test case:
1
3
5 1 1 1 1 1
3 1 1 2
3 2 1 1
2 1 1 1 1 1 1 1 1 2 1

Output:
Yes

'''

# Flawed recursive solution


def isValidOutput(stack_list, input_result):

    if not input_result:
        return True

    for element in stack_list:
        if element[element[0]] == input_result[0]:
            element[0] -= 1
            result_op = input_result.pop(0)
            if isValidOutput(stack_list, input_result):
                return True
            else:
                element[0] += 1
                input_result.insert(0, result_op)

    return False


def main():
    T = int(input())
    for _ in range(T):
        num_stacks = int(input())
        stacks = []
        i = 0

        while i < num_stacks:
            stacks.append(list(map(int, input().split())))
            i += 1

        output_string = list(map(int, input().split()))

        if num_stacks == 1:
            stacks[0].reverse()
            stacks[0].pop()
            if stacks[0] == output_string:
                print("Yes")
            else:
                print("No")
            continue

        if isValidOutput(stacks, output_string):
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()


'''
# Subsequence method


def rec_ans(ptrs, stp):
    global data, st
    if stp == -1:
        return True

    for i in range(len(ptrs)):
        if ptrs[i] < len(data[i]) and data[i][ptrs[i]] == st[stp]:
            ptrs[i] += 1
            if rec_ans(ptrs, stp - 1):
                return True
            ptrs[i] -= 1

    return False


from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
for _ in range(int(input())):
    n = int(input())
    data = []
    ptrs = [1] * n
    for i in range(n):
        data.append(list(map(int, stdin.readline().strip().split())))
    st = list(map(int, stdin.readline().strip().split()))
    if rec_ans(ptrs, len(st) - 1):
        print('Yes')
    else:
        print('No')

'''