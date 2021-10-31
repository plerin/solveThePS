'''

'''

for _ in range(int(input())):
    N, M = map(int, input().split())
    ret = 0
    for i in range(N, M+1):
        # ret += len([c for c in str(i) if c == '0'])
        ret += str(i).count('0')
    print(ret)
