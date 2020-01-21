# https://www.hackerearth.com/challenges/competitive/january-circuits-20/algorithm/set-numbers-bea74f5a/ (Accepted)


def NearestTwoPower(input_val):
    if input_val & (input_val + 1) == 0:
        return input_val

    count = 0
    while input_val != 0:
        count = count + 1
        input_val = input_val >> 1

    return 2 ** (count - 1) - 1


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(NearestTwoPower(N))