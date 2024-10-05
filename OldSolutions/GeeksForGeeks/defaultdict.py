# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
default_dict = defaultdict(list)

for i in range(1, n+1):
    input_str = input()
    default_dict[input_str].append(i)

for i in range(1, m+1):
    input_str = input()
    if len(default_dict[input_str]) == 0:
        print("-1")
    else:
        print(' '.join(map(str, default_dict[input_str])))

