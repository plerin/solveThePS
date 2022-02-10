'''
> P
N+1일에 퇴사를 하니까 N일까지 최대한 많은 벌이를 하고싶다 최대 수익은 얼마인가?
    - 상담 소요 일자와 수익이 매칭되어 입력된다.
> S
브루트 포스 _ 재귀로 풀이해보자
접근
    - 재귀 : 전체 문제를 부분 문제로 나눠서 바라보자 _ f(n) = n일 동안 벌 수 있는 최대 수익
    - bc : 
        - 조건 : if total == n+1
        - 로직 : print(money) // return
    - param : spend(int) : 필요 시간  // total(int) : 소요 일자 // moeny(int) : 현재까지 수익
    - logic
        1) spend가 0이면 해당 값(시간/소득)을 재귀 호출 하고 else 1 이상이면 -1 하고 상황봐
'''
import sys

input = sys.stdin.readline

# def solve(now:int, spend:int, money:int):
#     if now == N+1:
#         pass

#     for i in range(now,len(arr)):
#         spend -= 1
#         if spend == 0:
#             solve(now+1, i[0], money+i[1])
#         else:
#             solve(now+1, spend, money)


# N = int(input())
# arr = [map(int, input().split()) for _ in range(N)]
# solve(0,1,0,0)

# param : 일자 / 수익
def go(day: int, point: int):
    global ret

    if day >= n+1:
        if day == n+1:  # 마지막 날의 시간이 1일일 경우
            ret = max(ret, point) # 조건에 해당하는 경우 중 가장 큰 값을 남기기 위해 max 사용
        return # 마지막 날의 시간이 2일 이상인 경우 그냥 리턴 

    # 상담 하느냐
    go(day+t[day], point+p[day])
    # 안 하느냐
    go(day+1, point)


n = int(input())
# 시간 / 수익 리스트를 따로 만들었어 n+1로 -> ex) 7일이면 1~7일 그대로 사용할 수 있음
t = [0] * (n+1)
p = [0] * (n+1)
ret = 0

for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())

# 1일 / 수익 0부터 시작
go(1, 0)
print(ret)
