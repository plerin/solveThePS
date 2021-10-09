'''
goal : 3*N 크기 벽을 2*1, 1*2 타일로 채우는 경우의 수
1. 입력 받기
    1) N : 타일 열(COLUMN)
2. 로직_DP
    1) 최적해 : ai = 3*i를 채우는 타일의 경우의 수
    2) 최적부분구조(큰 문제를 작게 나누기) : 
'''


def dp(n):
    d[1] = 0
    d[2] = 3

    for i in range(3, n+1):
        d[i] = d[i-2]*2


N = int(input())

d = [0] * 31

ret = dp(N)

print(ret)
