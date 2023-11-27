# https://cses.fi/problemset/task/1090

n, x = list(map(int, input().split()))
p = sorted(list(map(int, input().split())))
out = 0

i, j = n - 1, 0
while j < i:
    if p[j] + p[i] <= x: j += 1
    out += 1
    i -= 1
    if i == j: 
        out += 1
        break

print(out)