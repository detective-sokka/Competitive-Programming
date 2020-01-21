# spoj.com ONP (Accepted)

T = int(input())
symbol_list = []

for _ in range(T):
    del symbol_list
    symbol_list = []
    expression = list(input())
    for element in expression:
        if 'a' <= element <= 'z' or 'A' <= element <='Z':
            print(element, end ="")
        elif element == '(':
            symbol_list.append(element)
        elif element == ')':
            while symbol_list[-1] != '(':
                print(symbol_list.pop(), end="")
            symbol_list.pop()
        else:
            symbol_list.append(element)

    while len(symbol_list) != 0:
        print(symbol_list.pop(), end="")
    print("\n", end="")




