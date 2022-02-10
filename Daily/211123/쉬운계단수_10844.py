'''
> P
인접한 모든 자리의 차가 1인 수를 계산 수라고 할 때
길이가 N인 계단 수가 총 몇개인지 구하시오
    - 0으로 시작하는 수는 계단 수가 아니다
> S
동적 계획법 _ 주어진 식을 풀어가며 패턴을 찾고 점화식 / dp 테이블 초기화 하자 

식을 풀어보니 이 문제도 수의 마지막 값이 무엇인지에 따라 결정되는 문제
    ex) 길이가 2이고 마지막 값이 3인 값은 43, 23 밖에 없다
    -> dp 테이블을 2차원 배열로 만들고 2차 배열 값을 마지막 값으로 풀이한다.

dp 테이블
dp[a][b] -> a : 길이 // b : 수의 마지막 숫자    ex) dp[2][3] = 길이가 2이고 마지막 수가 3인 수 == 43, 23
dp[1] = [0,1,1,1,1,1,1,1,1,1] 로 초기화
if b == 0: then dp[a][b] = dp[a-1][1]
if b == 9: then dp[a][b] = dp[a-1][8]
else then dp[a][b] = dp[a-1][b-1] + dp[a-1][b+1]

'''

MOD = 1000000000
MAX = 101

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(MAX)]

dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, MAX):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] % MOD
        elif j == 9:
            dp[i][j] = dp[i-1][8] % MOD
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD

print(sum(dp[N]) % MOD)
