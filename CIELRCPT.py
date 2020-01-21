# https://www.codechef.com/problems/CIELRCPT (Accepted)


def FindMinItems(input_price):
    items_bought = 0
    if input_price > 4095:
        items_bought += input_price // 2048
        input_price %= 2048

    while input_price != 0:
        if input_price & 1 == 1:
            items_bought += 1

        input_price = input_price >> 1

    return items_bought


def main():
    T = int(input())
    for _ in range(T):
        price = int(input())
        print(FindMinItems(price))


if __name__ == "__main__":
    main()