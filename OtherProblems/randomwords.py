# https://www.hackerearth.com/pt-br/problem/algorithm/random-words-17/


def sort_names(name_list):
    list_len = len(name_list)
    for i in range(list_len):
        for j in range(i+1, list_len):
            if len(name_list[i]) > len(name_list[j]):
                temp_name = name_list[i]
                name_list[i] = name_list[j]
                name_list[j] = temp_name

            elif len(name_list[i]) == len(name_list[j]):
                if name_list[i] > name_list[j]:
                    temp_name = name_list[i]
                    name_list[i] = name_list[j]
                    name_list[j] = temp_name


def main():
    N = int(input())
    names = []

    # for _ in range(N):
    #    names.append(input())

    names = input().split()

    sort_names(names)
    print('\n'.join(names))


if __name__ == '__main__':
    main()