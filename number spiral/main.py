t = int(input())

xy = []
for i in range(t):
    xy.append(input().split())

for i in xy:
    y = int(i[0])
    x = int(i[1])       
    if x > y: 
        if x % 2 == 0:
            print((x-1)**2 + y)
        else:
            print(x**2 - y + 1)
    else:
        if y % 2 == 0:
            print(y**2 - x + 1)
        else:
            print((y-1)**2 + x)
