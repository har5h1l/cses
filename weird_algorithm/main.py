def hailstone(start: int) -> str:
    sequence = [str(start)]
    while True:
        if start % 2 == 0:
            start = int(start / 2)
            sequence.append(str(start))
        elif start == 1:
            sequence = ' '.join(sequence)
            return(sequence)
        else:
            start = int(3 * start + 1)
            sequence.append(str(start))

start = int(input())
print(hailstone(start), end="")