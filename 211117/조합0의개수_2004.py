'''
> P
이항계수(n,m)의 끝자리 0의 개수를 출력
> S
이항계수 풀이 문제_ 수학
이항계수 점화식 + 동적계획법 활용
    - 점화식 1. dp[i][j] = dp[i-1][i] + dp[i-1][i-1] # nCk = n-1Ck + n-1Ck-1 
    - 점화식 2. dp[i][j] = choose(times+1,got) + choose(times+1,got+1) # 수를 뽑았는데 선택한 경우와 선택하지 않은 경우

함수(bino_coef)
    - purpose : n,m을 입력받아 해당 이항계수 값 반환
    - param : n(int) _ 개수 // m(int) : 선택 수
    - logic
        1. m 값 필터링 _ n보다 작은 경우 0 반환
        2. dp 테이블 초기화 _ (n+1)(n+1) _ -1 초기화  // (n+1)(r+1) _ 0초기화 2가지 방법으로 풀이
        3. 하향식 풀이 위한 dp 테이블 갱신
        4. (n+1) 이중 반복하며 점화식 적용 _ dp[i][j] = bino_coef() 
'''


def bino_coef(n, m):
    if n < m:
        return 0

    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    def choose(times, got):
        if times == n:
            return got == m

        if dp[times][got] != -1:
            return dp[times][got]

        dp[times][got] = choose(times+1, got) + choose(times+1, got+1)
        return dp[times][got]

    return choose(0, 0)


def bino_coef2(n, m):

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
    for i in range(m+1):
        dp[i][i] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    return dp[n][m]


n, m = map(int, input().split())

ret = bino_coef2(n, m)

print(ret)
