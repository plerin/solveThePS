'''
2가지 방법으로 풀어야지
1. 완전 탐색
시간 복잡도 : O(N!) -> 시간초과로 틀리지만 그래도 풀어보기

def bruteforce
    - param : start(int) _ 출발 도시,  depth(int)_ 누적 도시 개수, cost(int) : 누적 비용
    - vari : global ans(int) _ 결과 값 저장, 
    - logic
        1) bc : if depth == N then if graph[start][0] != 0 then ans = min(ans, cost+graph[start][0])
        2) for city in range(N) -> if city not visit and graph[start][city] != 0 then call func byself

2. 비트마스크(+DP)
A->B->C->D->E->F 와 A->C->B->D->E->F 는 D/E/F 가 중복된다 해당 값의 최적값을 저장해두고 사용

방문 확인을 비트(2bit)로 하자가 아이디어
각 도시 수마다 bitmask를 저장해두고 ex) 도시 3 -> [i][j] -> i = 3 , j = 1<<3(==2**3==8)

def dp
    - param : start(int) : 출발 도시, accumul(int) _ 누적 도시 개수
    - vari : global dp(list) : 사용할 dp 테이블 
    - logic
        1) if accumul == i<<n-1 then return graph[start][0] if graph[start][0] != 0 else INF
        2) if dp[start][accumul] != 0 then return dp[start][accumul]
        3) for i in range(n) -> if accumul >> i % 2 or graph[start][i] then continue
        4) tmp = dp(i, accumul | 1 << 1)
        5) cost = min(cost, tmp)
        6) end for
        7) dp[start][accumul] = cost
        return 
'''

INF = int(1e9)


def dfs(x: int, visited: int):
    global dp

    if visited == (1 << N) - 1:  # 모든 경로 들렸을 때 ex) n = 4 -> 1111(2)
        return graph[x][0] if graph[x][0] != 0 else INF

    if dp[x][visited] != INF:
        return dp[x][visited]

    for i in range(1, N):   # 출발지가 0이기 때문에 1부터 n~1까지
        if visited & (1 << i) or graph[x][i] == 0:
            continue
        dp[x][visited] = min(dp[x][visited], dfs(
            i, visited | (1 << i)) + graph[x][i])

    return dp[x][visited]


def bruteforce(start: int, depth: int, cost: int):
    global ans

    if depth == N:
        if graph[start][0] != 0:
            ans = min(ans, cost + graph[start][0])
        return

    for city in range(N):
        if city in visit or graph[start][city] == 0:
            continue
        visit.append(city)
        bruteforce(city, depth+1, cost+graph[start][city])
        visit.pop()


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# visit = [0]
# ans = INF
# bruteforce(0, 1, 0)
dp = [[INF] * (1 << N) for _ in range(N)]
# print(dp)
print(dfs(0, 1))
# print(dp)
# # print(ans)
