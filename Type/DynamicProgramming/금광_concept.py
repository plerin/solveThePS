'''
youtube url -> https://www.youtube.com/watch?v=5Lu34WIx2Us&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=6&t=2555s

>> Keyword
dp 이차원배열!
왼쪽의 값이 오른쪽에 영향을 준다면 문제를 풀 땐 오른쪽은 왼쪽에 영향을 받는다고 판단
    -> 방향은 오른쪽으로 진행, 오른쪽 위/옆/아래로 진행가능 == 왼쪽 위/옆/아래의 값에 영향을 받는다.
    -> dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

>> P
n*m 금광이 있을 때 1*1칸으로 나누어져있다. 
첫번째 열부터 오른쪽으로 이동하며 금을 캘 때 얻을 수 있는 금의 최대 크기
    - 이동은 오른쪽 위, 오른족, 오른쪽 아래로만 이동 가능

>> S
접근
1. 문제 유형 찾기
완전 탐색, 동적계획법
2. 점화식 구하기
arr[i][j] = i행, j열에 존재하는 금의 양
dp[i][j] = i행 j열 까지의 최적의 해(얻을 수 있는 금의 최댓값)
모든 좌표(위치)에서의 최적해를 구하면 됨, 고려사항은 왼쪽 위, 왼쪽, 왼쪽 아래에서 온 값을 처리한다는 것!!!
d[n][m] = arr[n][m] + max(dp[n-1][m-1] ,dp[n][m-1], dp[n+1][m-1])

코딩
1. 입력 받기 & dp 테이블 초기화 
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[int(input()) for _ in range(n)] for _ in range(m)]
2. col단위로 반복하며 row 단위로 읽으며 현재 dp 값 갱신

'''

for tc in range(int(input())):
    n, m = map(int, input().split())
    dp = [[int(input()) for _ in range(n)] for _ in range(m)]

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    ans = 0
    for i in range(n):
        ans = max(ans, dp[i][m-1])
    print(ans)
