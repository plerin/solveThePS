'''

풀이
1. dp 
ai = 정수 i를 1,2,3의 합으로 나타내는 방법의 수
ai = ai-1 + ai-2 + ai-3 , a1 = 1, a2 = 2, a3 = 4

dp = [0] * MAX(11)

- DP를 MAX 크기로 구해놓고 각 입력 값마다 바로 반환
func
    - param : n(int) : 입력 값
    - vari : global dp(list) : M

2. 완전탐색
같은 수도 반복할 수 있도록 재귀함수를 만들어
    - param : comb(list) _ 현재까지 선택된 조합 
    - vari : global n(int)
    - logic
        1) bc : if sum(comb) >= n then if sum(comb) == n then print(''.join(map(str,comb)))
        2) for i in range(1,4) -> comb.append(i) & recursive -> comb.pop()
'''

MAX = 11


def getDP():
    global dp

    for i in range(1, MAX):
        if i <= 2:
            dp[i] = i
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return


def dfs(comb: list):
    global ans

    if sum(comb) >= n:
        if sum(comb) == n:
            ans += 1
        return

    for i in range(1, 4):
        comb.append(i)
        dfs(comb)
        comb.pop()


for _ in range(int(input())):
    dp = [0 for i in range(MAX)]
    getDP()

    n = int(input())
    ans = 0

    print(dp[n])

    dfs([])
    print(ans)
