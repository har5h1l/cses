n = input()
nums = sorted([int(i) for i in input().split()])
 
i = 1
for num in nums:
    if i != int(num):
        print(i)
        exit()
    i = i + 1
print(n)

# A better, more efficient solution would be to use symmetric.difference with a set from 1 to n and a set that is missing the number.

# Another solution (even better) solution would be just to find the difference of the sum of the numbers from 1 to n (use n(n + 1)/2) and the sum of the numbers given (use sum()).