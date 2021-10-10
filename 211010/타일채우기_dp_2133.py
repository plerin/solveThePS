'''
goal : 3*N 크기의 벽을 2*1, 1*2 타일로 채우는 경우의 수
1. 입력
    1) N : 3*N의 N
2. 로직_DP
    1) 규칙찾기 : Ai = {(Ai-2)*3} + A0*2  _ i-2가 2가 될때가지 
    2) 점화식 : Ai = A2*3 + {Ai-2}
    3) 코드화
'''


def dp(n):
    d[1] = 0
    d[2] = 3

    for i in range(4, n+1, 2):
        d[i] = d[i-2]*3  # 맨 우측에 3*2 타일이 고정될 경우 이들 유형은 3개

        for j in range(4, i+1, 2):
            d[i] += d[i-j] * 2  # n=4부터는 새로운 도형이 2가지씩 추가된다.

    return d[n]


# 1
N = int(input())

d = [0] * 31

ret = dp(N)

print(ret)
