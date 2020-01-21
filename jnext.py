# spoj.com  JNEXT Accepted

'''
Test cases:
3
5
1 5 4 8 3
5
1 5 4 8 7 3
10
1 4 7 4 5 8 4 1 2 6

'''

T = int(input())

for _ in range(T):
    my_queue = []
    is_possible = False
    temp_var = 0
    N = int(input())
    array = list(map(int, input().split()))
    array_len = len(array)

    while len(array) > 1:
        my_queue.append(array.pop())
        if array[-1] < my_queue[-1]:
            is_possible = True
            for j in range(len(my_queue)):
                if array[-1] < my_queue[j]:
                    temp_var = array[-1]
                    array[-1] = my_queue[j]
                    my_queue[j] = temp_var
                    break
            break

    if is_possible:
        print("".join(map(str, array + my_queue)))
    else:
        print("-1")
