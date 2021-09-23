

N = input()
dishes = []
ret = 0

for d in N:
    ret = ret+10 if len(dishes) == 0 or dishes[-1] != d else ret+5
    dishes.append(d)

print(ret)
