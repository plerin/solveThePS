import sys
input = sys.stdin.readline

MAX = 10001

N = int(input())
ret = [0]*MAX

for _ in range(N):
    idx = int(input())
    ret[idx] += 1

for i in range(len(ret)):
    for _ in range(ret[i]):
        print(i, sep='\n')
