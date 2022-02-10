'''
> P 
정수 N을 1,2,3의 합으로 나타내는 방법의 수를 구하라
    - 같은 수를 2번 이상 연속해서 사용하면 안 됨
> S
동적 계획법

N을 나타내는 수의 조합에서 현재 값에 따라 이전 조합의 맨 뒤 값이 제한된다.
    ex) 현재 값이 1 이면 조합의 이전 마지막 값은 2,3이여야 한다 
    -> dp 테이블을 2차원 배열로 구성하여 [a][b] _ a = 정수 N, b = 조합의 마지막 값

점화식 
dp[n][0] = dp[n-1][1] + dp[n-1][2]  # n의 0으로 끝나는 조합의 방법 수 = n-1의 1로 끝나는 방법 수 + n-1의 2로 끝나는 방법 수
dp[n][1] = dp[n-1][0] + dp[n-1][2]
dp[n][2] = dp[n-1][0] + dp[n-1][1] 
단, 초기갑 갱신
dp[1] = [1,0,0] # [1][0] = 0+1
dp[2] = [0,1,0] # [2][0] = 1+1(x, 같은 수 연속) , [2][1] = 0+2
dp[3] = [1,1,1] # [3][0] = 2+1 // [3][1] = 1+2 // [3][2] = 0+3 

* 이차원 배열이 0~2인 이유는 1,2,3 3가지 경우이기 때문

DIV = 1000000009 로 초기화

상향식(bottom-up)
    - param : n(int) _ 방법의 수를 구할 정수
    - vari : global dp
    - logic
        1) dp 테이블 초기화
        2) for i in range(4, n+1) then dp[i-1][0/1/2] 초기화
        3) sum(dp[n]) % DIV 리턴
'''
import sys

input = sys.stdin.readline

DIV = 1000000009
MAX = 100001


def makeDP(dp: list):
    dp[1] = [1, 0, 0]
    dp[2] = [0, 1, 0]
    dp[3] = [1, 1, 1]

    for i in range(4, MAX):
        dp[i][0] = dp[i-1][1] % DIV + dp[i-1][2] % DIV
        dp[i][1] = dp[i-2][0] % DIV + dp[i-2][2] % DIV
        dp[i][2] = dp[i-3][0] % DIV + dp[i-3][1] % DIV


T = int(input())
nums = [int(input()) for _ in range(T)]
dp = [[0 for _ in range(3)] for _ in range(MAX)]

makeDP(dp)

for num in nums:
    print(sum(dp[num]) % DIV)
