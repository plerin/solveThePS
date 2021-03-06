'''
이항계수(binomial_coefficient) _ 주어진 크기 집합에서 원하는 개수만큼 순서 없이 뽑는 것
 * 이항 : 하나의 아이템에 대해 뽑거나 / 안 뽑거나 두 가지 선택만 있기 때문
 * ref : https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients
'''


# factorial 구현
def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

# 1번, nCk = n!/(n-k)!/k! (단, 0 <= k <= n)


def bino_coef_factorial(n, r):
    return factorial(n) // factorial(n-r) // factorial(r)  # 1번 수식

# 2번, nCk = n-1Ck + n-1Ck-1 => n개 중 k개 고르는 경우의 수 = 현재에서 선택 안 한 경우 + 현재에서 선택 한 경우 , k 조건은 위와 동일


def bino_coef(n, k):
    # 점화식에 의해 n이 2개와 같아지거나(2개중 2개 고르기) // k가 0이되면(n개중 0개 고르기) 모두 결과가 1이다.
    if k == 0 or n == k:
        return 1

    return bino_coef(n-1, k) + bino_coef(n-1, k-1)    # 3번 수식 이용


'''
# 3번
2번에 동적계획법 활용 _ cache를 [n+1][r+1] 사이즈로 만들고 0으로 초기화
k 조건 입력 _ n개 중 0개 뽑는 경우는 1 _ 하나도 뽑지 않는 경우 && n 개 중 n 개 뽑는 경우 _ 모두 뽑는 경우
반복문(n개중 k개 뽑는 경우)을 돌며 점화식 작성 _ 2번
'''
#


def bino_coef2(n, r):
    # cache에 담을 경우는 n은 0부터 n까지, k는 0부터 k까지 범위를 지니기 때문에 == 1~n개에서 1~k개 조합 찾기
    cache = [[0 for _ in range(r+1)] for _ in range(n+1)]

    # dp 테이블 초기화 _ 상향식 _ bottom-up
    for i in range(n+1):
        cache[i][0] = 1  # 총 몇 개이든 0개(하나도 뽑지 않는 경우)는 1이다
    for i in range(r+1):
        cache[i][i] = 1  # n개에서 n개(모두 뽑는 경우)를 뽑는 경우는 1이다

    # 귀납적 사고방식 => nCr = n-1Cr + n-1Cr-1 이고 nC0 =1 , nCn = 1이면  나머지에 대해서도 모두 합당하다
    for i in range(1, n+1):
        for j in range(1, r+1):
            # 점화식 2번 수식 == bino_coef(n-1,k) + bino_coef(n-1,k-1),
            cache[i][j] = cache[i-1][j] + cache[i-1][j-1]
            # n개가 있으면 n-1개 중 k개를 뽑는 경우(1개를 안뽑은 경우) + n-1개 중 k-1개 뽑는 경우(1개 뽑고 나머지 뽑는경우)

    return cache[n][r]  # cache를 (n+1)*(r+1)를 만들어놔서 [n][r] 그대로 사용 가능


'''
# 4번
n개 중 n번을 뽑는 경우 _ times(int) : 현재 뽑은 횟수 // got(int) : 선택한 개수
cache 선언 _ [n+1][n+1] n번 중 n번을 뽑음 && -1 : 아직 계산 안 함 || 나머지 : 계산 함 
'''


def bino_coef3(n, k):
    # k가 n보다 클 수 없으니 그런 경우 0 리턴
    if k > n:
        return 0
    # n개에서 n개를 선택하는 모든 경우를 계산하기 때문에 (n+1)*(n+1) // 부분문제 답이 저장되있는 경우만 반환 --> -1 == 초기화 값이고 이전에 계산하지 않았다는 의미
    cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    def choose(times, got):
        if times == n:
            return got == k  # n개를 뽑았는데 그 중 선택한 개수가 k라면 True 아니면 False

        if cache[times][got] != -1:  # 이전에 계산된 값(!= -1)이라면 그 값 반환_부분 문제
            return cache[times][got]

        # times 번까지 got 개를 선택했을 때 최종적으로 n 번의 개회를 소진해서 선택한 수가 k가 되는 경우의 수는 time+1번째에서 got을 선택했을 때(이번에 선택 안했을때) + time+1에서 got+1개가 선택된 경우(이번에 선택했을 때)의 합
        cache[times][got] = choose(times+1, got) + choose(times+1, got+1)

        return cache[times][got]

    return choose(0, 0)


print(bino_coef3(25, 12))
