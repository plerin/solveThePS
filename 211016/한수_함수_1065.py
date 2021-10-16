

N = int(input())

ret = 0

for i in range(1, N+1):
    if equalOrder(i) == True:
        ret += 1

print(ret)
