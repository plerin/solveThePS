'''
goal : 2*n 타일링을 1*2,2*1,2*2 타일 갖고 채우는 경우의 수 반환
1. 입력 받기
    1) N : 2*N의 열
2. 로직
    1) 최적해 : ai = 2*n 직사각형을 채우는 타일의 경우의 수
    2) 규칙 찾기 : i-1, i-2의 경우를 통해 작은 문제로 나눌 수 있음
    3) 점화식 : ai = ai-1 + ai-2 (a1 = 1, a2= 3)
    4) 코드화
'''

# 하향식


def dp(n):
    d[1] = 1
    d[2] = 3

    for i in range(3, n+1):
        d[i] = (d[i-1]+(2*d[i-2])) % 10007

    return d[n]

# 상향식


# def dp(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 3
#     if d[n] != 0:
#         return d[n]
#     else:
#         d[n] = (dp(n-1)+2*dp(n-2)) % 10007

#     return d[n]


N = int(input())

d = [0] * (1001)

ret = dp(N)

print(ret)
