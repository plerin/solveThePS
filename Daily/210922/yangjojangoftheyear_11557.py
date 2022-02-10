

# 반복하며 원하는 입력 받아
TEST = int(input())
ret = []
for i in range(TEST):
    NUM = int(input())
    grp = []
    for j in range(NUM):
        univ, cons = map(str, input().split())
        grp.append((univ, int(cons)))
    ret.append(sorted(grp, key=lambda x: x[1]).pop()[0])

for r in ret:
    print(r)
