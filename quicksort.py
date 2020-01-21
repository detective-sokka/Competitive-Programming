'''
Testcase:
10 5 9 4 3 2
10 9 8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8 9 10
1 8 9 3 7 5

'''


def partition(left, right, list_):
    if right <= left:
        return

    i = left
    j = right - 1
    pivot = right

    while i <= j:
        if list_[i] < list_[pivot]:
            i += 1
            continue
        elif list_[j] > list_[pivot]:
            j -= 1
            continue
        if i < j:
            temp = list_[i]
            list_[i] = list_[j]
            list_[j] = temp

    temp = list_[i]
    list_[i] = list_[pivot]
    list_[pivot] = temp

    return i


def QuickSort(left, right, list_):
    if left < right:
        pi = partition(left, right, list_)
        QuickSort(left, pi - 1, list_)
        QuickSort(pi + 1, right, list_)


def main():
    print("Enter the list to be sorted: ")
    input_list = list(map(int, input().split()))
    N = len(input_list)
    QuickSort(0, N-1, input_list)
    print(input_list)


if __name__ == '__main__':
    main()
