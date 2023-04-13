mars = [10.4,'#','%','@']
R = float(mars[0])    
for i in range(1, len(mars)):
        if mars[i] == '@':
            R *= 3
        elif mars[i] == '%':
            R += 5
        elif mars[i] == '#':
            R -= 7
    
print('%0.2f'%R)