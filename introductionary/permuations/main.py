n = int(input())

permutation = []
if n > 3:
    for i in range(2, n+1, 2):
        permutation.append(str(i))
    for i in range(1, n+1, 2):
        permutation.append(str(i))
    permutation = ' '.join(permutation)
elif n == 2 or n == 3:
    permutation = 'NO SOLUTION'
else:
    permutation = '1'

print(permutation)