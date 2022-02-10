'''
1~n 도시가 있을 때 모든 도시를 들리고 다시 출발 도시로 돌아오는 최소 비용 구하라
    - 도시 간 이동 비용이 다르다(a->b & b->a)
    - 도시 간 이동 불가능한 경우도 있다(==비용 0)

공통
1. 순회 == 출발지 상관 없다 == 0으로 지정
2. INF 선언 == int(1e9)
3. 

풀이1.dfs
1. visit = [False for i in range(N)] _ 방문 도시 체크(방문 전 = False , 방문 후 = True)
2. def findRoute1(start:int, depth:int) _ 출발 도시와 누적 도시 개수
    - bc : if depth == N then graph[start][0] else

풀이2.dp + 비트마스크
비트마스크로 방문 도시 체크 -> dp 테이블 적용 -> dp = [[INF] * (1<<N) for _ in range(N)] 
    - dp[i][j] => 현재 도시 i이고 현재 방문한 도시는 j이며 남은 방문하지 않은 도시 들렸다가 출발지로 돌아가는 최소 비용
    - 결국 구하는 게 dp[0][1](==현재 도시 0, 누적방문도시 0) 일 때의 최소 비용이기 때문에 뒤에서 앞으로 온다.
    - 점화식 => dp[i][j] = min(dp[i][j], dp[next][j + next] + graph[i][next])
    - def findRoute2(start:int, visit:int) _ 출발 도시와 누적 도시(비트마스크)
        - if visit == (1<<N) - 1 then return graph[start][0] if graph[start][0] != 0 else INF
        - if dp[start][visit] != INF then return dp[start][visit]
        - if visit & (1 << i) or graph[start][i] == 0 then continue
        - dp 
'''
import sys

INF = sys.maxsize


def findShorestRoute1(start: int, depth: int, cost: int):
    global ans, visit

    if depth == N:
        if graph[start][0] != 0:
            ans = min(ans, cost+graph[start][0])
        return

    for city in range(1, N):
        if visit[city] == True or graph[start][city] == 0:
            continue
        visit[city] = True
        findShorestRoute1(city, depth+1, cost+graph[start][city])
        visit[city] = False


def findShorestRoute2(start: int, visit: int):
    global dp

    if visit == (1 << N)-1:
        return graph[start][0] if graph[start][0] != 0 else INF

    if dp[start][visit] != INF:
        return dp[start][visit]

    for i in range(N):
        if visit & (1 << i) or graph[start][i] == 0:
            continue
        dp[start][visit] = min(dp[start][visit], findShorestRoute2(
            i, visit | (1 << i)) + graph[start][i])

    return dp[start][visit]


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# ans = INF
# visit = [False for _ in range(N)]
# visit[0] = True
# findShorestRoute1(0, 1, 0)
# print(ans)

dp = [[INF] * (1 << N) for _ in range(N)]

ans = findShorestRoute2(0, 1)

print(ans)
