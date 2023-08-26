# https://cses.fi/problemset/task/1622

def permutations(l):
    if len(l) == 1: return l
    
    # else

    x = l.pop() # adding this to each subperm
    subperms = permutations(l) # permutations of l with x removed
    out = []

    for p in subperms: # iterating through each permutation
        for i in range(len(p) + 1):
            completeperm = list(p)
            completeperm.insert(i, x)
            out.append(completeperm)
    
    return out

perms = sorted(set([''.join(p) for p in permutations(list(input()))]))

print(len(perms))
for p in perms: print(p)