
m, f = map(int, input().split())
ret = []
while max(m, f) != 0:
    ret.append(sum([m, f]))
    m, f = map(int, input().split())

for r in ret:
    print(r)
