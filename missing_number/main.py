n = input()
nums = sorted([int(i) for i in input().split()])
 
i = 1
for num in nums:
    if i != int(num):
        print(i)
        exit()
    i = i + 1
print(n)