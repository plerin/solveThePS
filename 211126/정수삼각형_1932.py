'''

MAX = n+1(501)

MAX가 500밖에 안되니까 DP 테이블을 2차원 배열로 만들고 갱신

점화식 => A[i][j] => i =  층(floor) // j = 층의 값들
A[i][j] = i층에 j 값은 i-1층 j-1/j 값의 영향을 받는다.


'''

MAX = 501


def solve(n: int, triangle: list):
    dp = [[0 for _ in range(n)] for _ in range(n)]

    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][0]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    print(dp)
    return max(dp[n-1])


n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

ret = solve(n, triangle)

print(ret)
