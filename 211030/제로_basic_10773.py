ret = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        ret.pop()
    else:
        ret.append(n)

print(sum(ret))
