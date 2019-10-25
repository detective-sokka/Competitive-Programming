# codechef code - LAPIN
T = int(input())
# print(range(T))
for i in range(T):
    input_str = input()
    str_length = len(input_str)
    half_length = str_length // 2
    left_str = input_str[0:half_length]
    if str_length % 2 == 1:
        right_str = input_str[(half_length+1):]
    else:
        right_str = input_str[half_length:]
    left_str = ''.join(sorted(left_str))
    right_str = ''.join(sorted(right_str))
    if left_str == right_str:
        print("YES")
    else:
        print("NO")
