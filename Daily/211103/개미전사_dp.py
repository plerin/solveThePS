'''
[P]
N개로 이뤄진 창고를 털어보자 얻을 수 있는 최대 식량 값?
    - 최소 한 칸 이상 떨어진 창고 약탈해야함
[S]
최댓 값을 구하는데 어떤 접근으로 풀 수 있는가? 딱 떠오르는 건 그리디 / 완전 탐색
    - 최소 한 칸이상 떨어진 창고를 선택함에 있어서 최적의 해를 구하는 방법이 있는가 (그리디) -> 음??
    - 없으면 DP로 접근해보자 i번째 선택하기 위해 점화식 -> ai = max(ai-1, ai-2 + k(현재값))
    - 점화식을 구했다면 dp 조건 2개 모두 만족하는가?
        - 최적 부분 문제 : 큰 문제를 작은 문제로 나눠 풀 수 있는가 -> 0
        - 중복 부분 문제 : 큰 문제가 여러 중복되는 문제로 나뉘는가 -> 0
[l]
점화식을 사용하여 로직 구현하자
    - 점화식 : ai = max(ai-1, ai-2 + k) a[0] / a[1] 은 지정된 값 -> 바텀업(하향식) 풀이
1. 입력 받기
    - N(INT) : 식량창고 개수
    - K(LIST) : 창고에 저장된 식량
2. DP 준비
    - VARIABLE : DP(LIST) - 크기 : LEN(K) _ 0으로 초기화 
    - PARAM :  n(int) _ 식량창고 수
    - logic : 점화식 구현
    - return : 최댓 값
'''


def solve(n):
    global K
    dp = [0] * len(K)

    dp[0] = K[0]
    dp[1] = max(K[0], K[1])

    for i in range(2, len(K)):
        dp[i] = max(dp[i-1], dp[i-2]+K[i])

    return dp[n-1]


N = int(input())
K = list(map(int, input().split()))

ret = solve(N)

print(ret)
