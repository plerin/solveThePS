'''
> P 
N개 정수로 이루어진 수열에서 연속 수의 최대 합을 구하라
> S
동적 계획법 _ dp 테이블 갱신하며 풀자

MAX = 100001

이전까지의 최대 합을 알아야 함과 동시에 그 때까지의 모든 합을 알아야 함 => 2차원 배열
a[i][j] => i = 수열 길이 // j[0] = 현재 길이(i)까지의 최대 길이 합 // j[1] = 현재 길이(i)까지 최대 길이 조합의 합
점화식 -> a[i][j] = max(a[i-1][0], a[i-1][1] + now, now) 단, a[0] = [seq[0], seq[0]] 

상향식(bottomUp)
풀이
    1) dp 테이블 초기화 // dp = [0] * MAX
    2) 함수 호출
    3) dp 테이블 초기값 갱신 && 수열 길이 만큼 반복
    4) 만약 현재 값이 이전 dp값보다 크다면 dp 테이블 현재 값으로 초기화
'''


n = int(input())
seq = list(map(int, input().split()))

# sum = [seq[0]]  # 첫 번째 값으로 초기화 비교를 위해

# for i in range(n-1):
#     sum.append(max(sum[i]+seq[i+1], seq[i+1]))


dp = [0] * n

dp[0] = seq[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+seq[i], seq[i])

print(max(dp))
