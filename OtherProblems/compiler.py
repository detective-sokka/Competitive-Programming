# codechef.com  Problem Code - COMPILER (Accepted)

T = int(input())


def checkExpression(input_expression):
    exp_len = 0
    temp = 0
    for i in range(len(input_expression)):
        if input_expression[i] == '<':
            temp += 1
        else:
            temp -= 1
            if temp == 0:
                exp_len = max(exp_len, i+1)
            elif temp < 0:
                break
    return exp_len


for _ in range(T):
    stack_ = []
    expression = list(input())
    print(checkExpression(expression))




