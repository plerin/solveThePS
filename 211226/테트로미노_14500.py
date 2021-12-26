'''
>> P
1*1 4개로 이어진 도형을 테트로미노라고 할 때, N*M 위 하나를 넣아 해당 정사각형 값이 최대인 경우 구하라

>> S
도형이 그려져 있고 이 도형의 모든 경우의 수를 어떻게 구하지 겁먹었던 문제
사실 그럴 필요 없이 N*M 그래프를 탐색하면 모든 경우를 구할 수 있어 
    -> DFS를 4번 탐색하면 모든 경우(ㅗ 모형제외)를 구할 수 있다.
    -> 도형의 모양에 크게 상관 할 필요 없어(ㅗ 모형제외)
    -> ㅗ 모형은 일반적인 DFS로 구할 수 없어 특수한 로직 필요(이어 그리기 해보면 알아 ㅗ는 한 번에 이어 못그려)

>> F
DFS 풀이 
1. 입력 값 변수 초기화
2. visited(list)로 N*M 만큼 False로 초기화 & 방향벡터 변수
3. N*M만큼 탐색하며 방문
4. dfs 함수 호출
    - param: depth:int, total:int, x:int, y:int
    - vari: global ans(int)
    - logic
        1) bc : if depth == 4 -> update ans
        2) for (dx, dy) in [방향벡터]
            -> nx = x + dx, ny = y + dy
            -> check range & visited() -> if depth == 2 -> 본인자리 serach  &  다음 자리search

'''


def dfs(depth: int, total: int, x: int, y: int):
    global visited, ans

    if total + ((4 - depth) * max_val) < ans:
        return
    if depth == 4:
        ans = max(ans, total)
        return

    for (dx, dy) in move:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if depth == 2:
                # ㅗ 모형일 때 처리 _ 제자리에서 한 번 더 탐색해야 얻을 수 있음
                visited[nx][ny] = True
                dfs(depth+1, total+graph[nx][ny], x, y)
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(depth+1, total+graph[nx][ny], nx, ny)
            visited[nx][ny] = False


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0

max_val = max(map(max, graph))

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(1, graph[i][j], i, j)
        visited[i][j] = False

print(ans)
