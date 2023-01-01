n = input()
nums = sorted([int(i) for i in input().split()])
 
i = 1
for num in nums:
    if i != int(num):
        print(i)
        exit()
    i = i + 1
print(n)

# A better and more efficient solution would be to use symmetric.difference with a set from 1 to n and a set that is missing the number, but this solution works fine (it is slower though).