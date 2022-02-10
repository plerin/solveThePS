
n = int(input())

for _ in range(n):
    num, s = map(str, input().split())
    print(''.join(list(map(lambda x: x*int(num), map(str, s)))))
