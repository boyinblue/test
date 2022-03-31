nlist = [0, 1, 2, 3, 42, 43, 44, 45]
mlist = []

def mod42(input):
    return input % 42

print(nlist)
mlist = list( map( mod42, nlist) )
print(mlist)
