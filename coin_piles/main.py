# https://cses.fi/problemset/task/1754

for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if (2 * a - b) >= 0 and (2 * b - a) >= 0 and (2 * a - b) % 3 == 0 and (2 * b - a) % 3 == 0: print('YES')
    else: print('NO')