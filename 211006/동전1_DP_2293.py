'''
GOAL : N가지 종류의 동전으로 K만드는 경우의 수 반환
    1) 동전은 각각 다르고 입력으로 주어짐
1) 

'''

N,K = list(map(int,input().split()))
coin = [int(input()) for _ in range(N)]

d = [0]*10000
d[1] = 1
for i in range(2,10):
    if i >= 4:
        d[i] = d[i-1]+d[i-2]+d[i-5]
    else:
        d[i] = d[i-1]+d[i-2]

print(d[K-1])