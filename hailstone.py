def hailstone(x):
    nums = [x]
    try:
        x = int(x)
    except:
        return('Bad Input.')
    while True:
        if x % 2 == 0:
            x = int(x / 2)
            nums.append(str(x))
        elif x == 1:
            nums = ' '.join(nums)
            return(nums)
        else:
            x = int(3*x + 1)
            nums.append(str(x))

while True:
    x = input('Enter Num: ')
    print(hailstone(x))