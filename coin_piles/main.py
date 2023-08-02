# https://cses.fi/problemset/task/1754

for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    while True:
        if a > b:
            a, b = a - 2, b - 1
        elif b > a:
            a, b = a - 1, b - 2
        if a < 0 or b < 0:
            print('NO')
            break
        if a == b:
            if a % 3 == 0: print('YES')
            else: print('NO')
            break