'''
[P]
N가지 종류의 화폐가 있고 개수를 최소한으로 사용해서 가치의 합이 M인 되도록 만든다.
[S]
그리디는 어려운 게 어떤 화폐가 주어질지 모르니까 그 때마다 최적의 선택을 하기 어려워
다이나믹으로 접근해보자
    - ai = i원을 만들기 위한 최소 화폐 개수 // k = 화폐 단위
    - 점화식(k만큼 반복)
        - ai-k를 만들 수 있다면 ->  ai = min(ai,ai-k+1)
        - ai-k를 만들 수 없다면 -> ai = INF(임의의 무한 값)
    - 시간 복잡도 : O(N*M)
[L]
1. 키포인트
    - DP테이블을 사용하는데 임의의 MAX 값으로 N+1개수만큼 초기화해
    - 점화식을 구현(N만큼 반복하며 DP 테이블 갱신)
2. 입력 받기
    - N(INT) : 화폐 종류 // M(INT) : 만들어야 하는 가치
    - bills(list) : 화폐
3. 동적계획법 준비물
    - 변수 : INF(INT) : 여기선 10001(M 최대값 +1) // dp(list) : INF으로 N+1만큼 초기화
    - 로직
        1) BILLS를 반복하며 지정 화폐마다 가치(1~INF)의 DP 테이블을 갱신해
        2) 점화식 이용
4. 결과 추력
'''
# 임의의 최대 값을 문제 조건에서 갖고와
INF = 10001

# 입력 받기
N, M = map(int, input().split())
bills = [int(input()) for _ in range(N)]
# dp 테이블은 INF 값으로 M+1 까지 초기화
dp = [INF] * (M+1)

# 하향식(바텀업)으로 풀기 위해서 기본 값 갱신이 필요해 _ ai = min(ai, ai-k+1)이기 때문에 ai-k의 최소 값을 0으로 갱신
dp[0] = 0

for i in range(N):
    # biils[i]부터 시작해야지 만약 1부터 시작하고 biils[0]이 2이상이면 인덱스가 -가 나와 오류발생
    for j in range(bills[i], M+1):
        if dp[j - bills[i]] != INF:  # ai-k 가 INF가 아니라면 ==> 갖고 있는 화폐로 구성할 수 있다면
            dp[j] = min(dp[j], dp[j-bills[i]]+1)  # 점화식 : Ai = min(Ai, Ai-k+1)

if dp[M] == INF:
    print(-1)
else:
    print(dp[M])


'''
문제 정리
- N가지 화폐를 활용해 M원을 만들 때 최소 화폐 개수를 구하라

주어지는 화폐 값이 어떤 값인지 모르니 그리디는 사용 못해
DP로 접근해보자

'''

INF = 10001

N, M = map(int, input().split())
bills = [int(input()) for _ in range(N)]
dp = [INF] * (M+1)

dp[0] = 0

for i in range(N):
    if j in range(bills[i], M+1):
        if dp[j - bills[i]] != INF:
            dp[j] = min(dp[j], dp[j - bills[i]] + 1)

if dp[M] == INF:
    print(-1)
else:
    print(dp[M])
