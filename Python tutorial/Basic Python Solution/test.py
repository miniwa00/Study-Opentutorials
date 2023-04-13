import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    math_expression = list(map(str, sys.stdin.readline().rstrip().split()))
    
    math_expression[0] = float(math_expression[0])
    
    for i in range(1, len(math_expression)):
        if math_expression[i] == '@':
            math_expression[0] *= 3
        elif math_expression[i] == '%':
            math_expression[0] += 5
        elif math_expression[i] == '#':
            math_expression[0] -= 7
    
    print("{:.2f}".format(math_expression[0]))