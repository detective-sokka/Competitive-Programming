# https://www.codechef.com/problems/ALTARAY (Accepted)


def CheckAlternating(a, b):
    if a >= 0 and b < 0:
        return True
    elif a < 0 and b >= 0:
        return True
    else:
        return False


def Alt_SubArray_Count(input_list, input_len):
    list_ = [1] * input_len
    i = input_len - 2

    while i >= 0:
        if CheckAlternating(input_list[i], input_list[i + 1]):
            list_[i] += list_[i + 1]
        i -= 1

    return map(str, list_)


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        print(' '.join(Alt_SubArray_Count(arr, len(arr))))

