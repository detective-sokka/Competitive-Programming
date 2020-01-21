# https://discuss.codechef.com/t/a-tutorial-on-fast-modulo-multiplication-exponential-squaring/2899


def fast_exponent(b, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        return fast_exponent(b * b, exp // 2) % 1000000007
    else:
        return (b * fast_exponent(b * b, (exp-1) // 2)) % 1000000007


def without_recursion(b, exp):
    res = 1
    MOD = 1000000007
    while exp > 0:
        if exp % 2 == 1:
            res = (res * b) % MOD
            exp -= 1
        b = (b * b) % MOD
        exp /= 2

    return res % MOD


print("Enter base and exponent: ", end="")
[base, exponent] = map(int, input().split())

print("\nUsing the fast exponent method : ", fast_exponent(base, exponent))
print("\nUsing the fast exponent method without recursion : ", without_recursion(base, exponent))