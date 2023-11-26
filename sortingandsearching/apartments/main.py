# https://cses.fi/problemset/task/1084

n, m, k = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
out = 0
i, j = 0, 0

while i < n:
    x = a[i]
    r1, r2 = x - k, x + k
    while j < m:
        y = b[j]
        if y >= r1 and y <= r2:
            out += 1
            i += 1
            j += 1
            break
        elif y < r1:
            j += 1
        elif y > r2:
            i += 1
            break
    if j >= m: break

print(out)
