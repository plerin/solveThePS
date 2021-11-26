'''
> P
0~N인 정수에서 K개를 더해서 N을 만드는 방법의 수 찾아라
> S

n과 k의 관계를 점화식을 풀어가야 함 ==> 변수 2개 ==> 2차원 배열
aik = 0~i인 정수에서 k개를 더해서 i를 만드는 방법의 최적의 해
점화식 -> aik = a[i-1][k] + a[i][k-1] 단, i,k는 1부터 시작(초기화 필요)
i =1 이면 k 값 상관없이 k(0과 조합하면 k개)
k = 1 이면 i 값 상관 없이 1(i 자기 자신)

MAX = 201
dp = [[0] * MAX for _ in range(MAX)]    # MAX * MAX 2차원 배열 _ 초기값은 0이여도 상관 없어

'''
MAX = 201


def bottomUp():
    global dp

    for i in range(1, MAX):
        dp[1][i] = i
        dp[i][1] = 1
    for i in range(2, MAX):
        for j in range(2, MAX):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[N][K]


N, K = map(int, input().split())
dp = [[0] * MAX for _ in range(MAX)]

ret = bottomUp()

print(ret % 1000000000)
