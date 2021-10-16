import sys

input = sys.stdin.readline

for i in range(1, int(input())+1):
    a, b = map(int, input().split())
    print('Case #{idx}: {n1} + {n2} = {n3}'.format(idx=i, n1=a, n2=b, n3=a+b))
