sequence = input()

maxlen = 0
length = 0
prev_char = None
for char in sequence:
    if char == prev_char:
        length += 1
    else:
        if length > maxlen:
            maxlen = length
        length = 1
    prev_char = char
if length > maxlen:
    maxlen = length
 
print(maxlen)