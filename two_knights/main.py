n = int(input())

subtract = 8
for k in range(1, n+1):
    subtract += (k-2)*8
    print(int((k**2)*(k**2 - 1)/2 - subtract))