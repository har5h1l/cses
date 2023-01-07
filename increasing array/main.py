n = int(input())
array = [int(i) for i in input().split()]

moves = 0
for i in range(0, n - 1):
    if array[i] > array[i + 1]:
        moves += array[i] - array[i + 1]
        array[i + 1] = array[i]

print(moves)