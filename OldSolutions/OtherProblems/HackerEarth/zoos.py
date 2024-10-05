# hackerearth.com Zoos Problem [November circuits] (Accepted)

input_word = list(input())

word_len = len(input_word)

x_count = 0
y_count = 0

# to count number of zs
for i in range(word_len):
    if input_word[i] == 'o':
        break
    elif input_word[i] != 'z':
        x_count = -1
        break
    x_count += 1

for j in range(i, word_len):
    if input_word[j] != 'o':
        y_count = -1
        break

    y_count += 1

if y_count == x_count * 2:
    print("Yes")

else:
    print("No")

