# https://cses.fi/problemset/task/1755

n = input()
x = set(n)
l, m = '', ''
out = None

for i in x:
    if i in l or i == m: continue

    o = n.count(i)
    if o % 2:
        if len(m) >= 1: 
            out = 'NO SOLUTION'
            break
        else:
            m = i
            l += int((o - 1)/2) * i
    else:
        l += int(o/2) * i

if out != 'NO SOLUTION': print(l + m + l[::-1])
else: print('NO SOLUTION')
