# https://www.codechef.com/problems/STICKS (Accepted)


def MaxRectangle(input_array):
    array_frequency = [0] * 1001
    for element in input_array:
        array_frequency[element] += 1

    i = 1000
    x = 0
    y = 0
    while i >= 1:
        if 1 < array_frequency[i] < 4:
            if x == 0:
                x = i

            elif y == 0:
                y = i
                break
        elif array_frequency[i] >= 4:
            if x == 0 and y == 0:
                return i * i

            elif y == 0:
                return x * i

        i -= 1

    if x * y == 0:
        return -1

    return x * y


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        array = map(int, input().split())
        print(MaxRectangle(array))


if __name__ == "__main__":
    main()