'''
> P
N가지 종류의 화폐가 있고 최소한으로 사용해서 M원을 만드려고 할 때 m원을 만들기위한 최소 화폐 개수 출력
    - 불가능한 경우 -1 출력
> S
동적계획법
> L
최적 부분 문제 / 중복 부분 문제 모두 만족하는 지 확인 
ai = i원을 만들기 위한 최적의 해(최소 화폐 개수) // bi = i번째 화폐 가치
ai = min(ai-b1, ai-b2, .... ai-bn) + 1 , a0 = 0

하향식(top-down) - 재귀
    - param : m(int) _ 만들어야 하는 값
    - vari : 전역변수 _ bills(list) / global dp(list)
    - bc : if m == 0 then return 0
    - logic
        1) if dp[m] != 0 then return dp[m]
        2) for bill in bills then dp[m] = min(dp[m-bill], dp)

상향식(botton-up) - 반복

'''
MAX = 10001  # MAX 값은 이 문제 범위의 최대 값 + 1


def solve(m):
    global dp
    if m == 0:
        return 0
    if m < 0:
        return MAX

    if dp[m] != MAX:
        return dp[m]

    for bill in bills:
        dp[m] = min(dp[m], solve(m-bill) + 1)

    return dp[m]


def solve2(m):
    global dp

    dp[0] = 0

    for bill in bills:
        for j in range(bill, m+1):  # bill부터 시작한다는게 핵심!
            if dp[j - bill] != MAX:
                dp[j] = min(dp[j], dp[j - bill] + 1)

    return dp[m]


N, M = map(int, input().split())
bills = [int(input()) for _ in range(N)]

dp = [MAX] * (M+1)  # 위와 같은 문제인 경우 min을 담아야 하기 때문에 dp 기본 값을 MAX 값으로 초기화

# dp[0] = 0   # 0을 만드는데 필요한 화폐의 개수 = 0

# for i in range(N):
#     for j in range(bills[i], M+1):  # 화폐 금액(bills[i])부터 M원까지
#         # j원에서 화폐 금액을 뺀 값을 만들 수 있는 경우가 있다면 ( 디폴트가 MAX이기 때문에 MAX가 아니다 == 만드는 경우가 존재한다)
#         if dp[j - bills[i]] != MAX:
#             dp[j] = min(dp[j], dp[j - bills[i]] + 1)


# if dp[M] == MAX:
#     print(-1)
# else:
#     print(dp[M])


print(solve(M))
