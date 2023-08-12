n = int(input())

for i in range(2 ** n): 
    a = bin(i)[2:].zfill(n)
    b = '0' + a[:-1]
    c = ''

    for i in range(n):
        if a[i] == b[i]: c += '0'
        else: c += '1'
    
    print(c)