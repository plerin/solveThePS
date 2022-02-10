A, B = map(int, input().split())
ret = ''

while max(A, B) != 0:
    ret = ret+'Yes\n' if A > B else ret+'No\n'
    A, B = map(int, input().split())

print(ret[:-1])
