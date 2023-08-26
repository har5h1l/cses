n = int(input())

if n*(n+1)/2 % 2 == 0: # if all nums can be divided into two equal sets
    print('YES')
    set_one = []
    set_two = []
    if n % 2 == 0: # if n is even we loop through nums from 1 to n
        x = n + 1
    else: # if n is odd we loop through nums from 1 to n -1, and add n to second set
        x = n
        set_two.append(str(n))
    for i in range(int(n/2)):
        if i % 2 == 0:
            set_one.append(str(i + 1))
            set_one.append(str(x - i - 1))
        else:
            set_two.append(str(i + 1))
            set_two.append(str(x - i -1))
    print(len(set_one))
    print(' '.join(set_one))
    print(len(set_two))
    print(' '.join(set_two))
else:
    print('NO')