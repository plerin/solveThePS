'''
> P
N+1일에 퇴사하려고 하는데 남은 N일 동안 최대한 많은 수익 구하는 프로그램 구하기
    - 일자별 소요일자와 금액이 나와있다.

> S
1. 재귀
today(int) 를 넘기고 profit(int)와 day(int)를 누적하며 계산

def getMaxProfit1(today:int, day:int, cost:int):
    if day >= N:
        cost = cost if day == 7 else cost-board[6][1]:
        ans = max(ans, cost)
        return
    
    for i in range(today, N):
        getMax(board[i][0],day + board[i][0], cost + board[i][1])

'''


def getMaxProfit1(today: int, cost: list):
    global ans
    if today >= N:
        if today == N:
            ans = max(ans, sum(cost))
        else:
            ans = max(ans, sum(cost[:-1]))
        return

    for i in range(today, N):
        cost.append(board[i][1])
        getMaxProfit1(i + board[i][0], cost)
        cost.pop()


# def getMaxProfit2(today: int, cost: list):
#     global dp

#     if today >= N:
#         return sum(cost) if today == N else sum(cost[:-1])

#     if dp[today] != 0:
#         return dp[today]


#     for i in range(N):
#         (day, profit) = board[i]
#         # profit =
#         if i == 0:
#             dp[i+day] = dp[i] + profit
#         cost.append(board[i][1])
#         dp[i] =
#         getMaxProfit1(i + board[i][0], cost)
#         cost.pop()

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
getMaxProfit1(0, [])

# dp = [0 for _ in range(N)]

print(ans)
