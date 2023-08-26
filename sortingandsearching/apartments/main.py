# https://cses.fi/problemset/task/1084

n, m, k = list(map(int, input().split()))
a = list(map(lambda x: (int(x)-k, int(x)+k), input().split()))
b = list(map(int, input().split()))