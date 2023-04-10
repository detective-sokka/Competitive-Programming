# Problem - https://www.hackerearth.com/challenges/competitive/october-circuits-19/algorithm/ap-1-f43562f4/

"""
Sample inputs:
7 2
1 2 3 5 6 7 8
1 7 1
4 4 3

8 3
8 7 6 0 1 2 3 4
1 8 -1
1 4 -1
1 8 1
"""

_, num_queries = [int(x) for x in input().split()]

array = list(map(int, input().split()))

for _ in range(num_queries):
    left, right, difference = [int(x) for x in input().split()]

    if left == right:
        print("1")
        continue

    max_length = 0
    segment_length = 1

    previous = array[left - 1]
    for current in array[left:right]:
        if current == previous + difference:
            segment_length += 1

        else:
            max_length = max(max_length, segment_length)
            segment_length = 1
        previous = current

    max_length = max(max_length, segment_length)
    print(max_length)
