'''
Testcase:
10 5 9 4 3 2
'''


def bubbleSort(input_list):
    i = 0
    N = len(input_list)
    for i in range(N-1):
        for j in range(0, N - i - 1):
            if input_list[j] > input_list[j+1]:
                temp_var = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = temp_var


def main():
    list_ = []
    print("Enter the list to be sorted: ")
    list_ = list(map(int, input().split()))
    bubbleSort(list_)
    print(list_)


if __name__ == "__main__":
    main()