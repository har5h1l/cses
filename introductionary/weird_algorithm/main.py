start = int(input())

sequence = [str(start)]
while start != 1:
    if start % 2 == 0:
        start = int(start / 2)
        sequence.append(str(start))
    else:
        start = int(3 * start + 1)
        sequence.append(str(start))
sequence = ' '.join(sequence)

print(sequence, end="")