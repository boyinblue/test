import random

letters=["a", "b", "c", "d"]

print("lens : ", len(letters))

cnt = 0
while cnt < 20:
    print("rand : ", random.randrange(0, 4))
#    print("rand : ", random.randrange(0, len(letters)))
    cnt = cnt + 1
