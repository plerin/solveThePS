'''
> P
m,n,x,y가 입력 값으로 주어진다.
m,n은 최대 값
x,y는 각각 m,n을 최대 값으로 삼는 값이다.
    -> m이 10이고 x는 10밖에 표현 못하고 x는 11일 때 1로 표현된다.

> S
브루트 포스

> l
1. 테스트 경우 마다 함수 호출
2. 함수
    - param : m,n, x, y (x,y의 max값)
    - logic
        1) 1부터 m,n 값이 나올 때까지 x,y 값 구해
        2) if i, j == x,y then return val else -1

how to cal x, y
x = val % m if val % m != 0 else val
y = val % n if val % n != 0 else val
'''
import sys

input = sys.stdin.readline


# def calDate(m: int, n: int, x: int, y: int):
#     if m == x and n == y:
#         return 1

#     i, j = 0, 0
#     val = 0

#     while True:
#         if (i, j) == (m, n) or val == 40001:
#             return -1
#         elif (i, j) == (x, y):
#             return val

#         val += 1

#         i = val % m if val % m != 0 else m
#         j = val % n if val % n != 0 else n

def calDate(m, n, x, y):
    ans = 0

    while x <= m*n:
        if x % n == y % n:
            ans = x
            break
        x += m

    return ans if ans != 0 else -1


for _ in range(int(input())):
    m, n, x, y = map(int, input().split())

    ret = calDate(m, n, x, y)

    print(ret)
