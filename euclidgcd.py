def gcd(a, b):
    if a == 0:
        return b

    gcd(b % a, a)


print("Input two numbers : ", end="")
[x, y] = map(int, input().split())
print("The GCD is : ", end="")

res = gcd(x, y)

print(res)
