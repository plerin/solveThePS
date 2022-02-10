

ret = []
for _ in range(3):
    ret.append(input())

print(eval(''.join(ret)))

# 이렇게도 풀려
# exec('print('+input()+input()+input()+')')