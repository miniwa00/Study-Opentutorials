T = int(input())

for _ in range(T):
    mars = list(map(str,input().split()))
    R = float(mars[0])
    
    for i in range(1, len(mars)):
        if mars[i] == '@':
            R *= 3
        elif mars[i] == '%':
            R += 5
        elif mars[i] == '#':
            R -= 7
    
    print('%0.2f'%R)