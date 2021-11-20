'''
최소 한 칸 이상 떨어진 식량창고 약탈 

ai = i개 식량창고를 약탈하여 얻을 수 있는 최대 값, k = i번째 약탈 식량 값 
점화식 : ai = max(ai-1, ai-2+k)

하향식(재귀)
    - param : n(int) _ 식량 창고
    _ base-condition : if n == 1 || n == 2 then return max(seq[:n])
    _ logic
        1) if dp[n] != 0: then return dp[n]
        2) dp[n] = max(dp[n-1], dp[n-2]+arr[n])

상향식(반복)
    - param : none
    - vari : N(global)
    - logic    
        1) dp[1],dp[2] init
        2) for i in range(3,N+1): then dp[i] = max(dp[i-1], dp[i-2]+arr[i])
'''
# MAX = 1001 # 제함 범위의 최대 값


# 하향식(top-down) _ 재귀
def func1(n: int):
    global store

    if n == 1 or n == 2:
        return max(store[:n])

    if dp[n] != 0:
        return dp[n]

    dp[n] = max(func1(n-1), func1(n-2)+store[n-1])

    return dp[n]

# 상향식(bottom-up) _ 반복


def func2():
    global store

    dp[1], dp[2] = store[0], max(store[:2])

    for i in range(2, N+1):
        dp[i] = max(dp[i-1], dp[i-2]+store[i-1])

    print(dp)
    return dp[N]


N = int(input())
store = list(map(int, input().split()))

dp = [0] * (N+1)

ret1 = func1(N)
ret2 = func2()

print(ret1, ret2)
