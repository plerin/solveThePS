'''
>> P
N*M 위에 정사각형을 4개 이어 붙인 테트로미노를 하나 놓았을 때 해당 범위의 합잉 가장 큰 경우
    - 정사각형은 변끼리 모두 연결되있어야 한다.
>> S
1. 모든 도형은 4번 탐색하면 모두 만들 수 있다(ㅗ 모형 제외)
    - 'ㅗ' 모형은 못그려 _ 한 점 그리고 그려봐 못그려 -> 로직 필요
        -> 2번 탐색 후 제자리 탐색을 해야함
2. N*M에서 가장 큰 값을 구한 뒤 현재까지 구한 값에 앞으로 남은 탐색 횟수 * MAX값 구해서 작으면 return(가지치기 == 백트래킹)
    - max_v = max(map(max,graph))
    - DFS 함수에 기저 조건으로 추가

>> F
common
visited = [[False] * M for _ in range(N)]
max_val = max(map(max, graph))
ans = -1e9

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs()
        visited[i][j] = False

def dfs(depth: int, total: int, x: int, y: int):
    - vari : global visited, ans
    - logic
        1) bc#1 : if total + (4 - depth) * max_val < ans  -> return
        2) bc#2 : if depth == 4 -> update ans & return
        3) for (dx, dy) in move:
            => if check range and not visited 
                -> if depth == 2: ('ㅗ'모형 처리) & 모든 모형 처리

'''


def dfs(depth: int, total: int, x: int, y: int):
    global visited, ans

    # 앞으로 탐색 횟수에 max 값을 곱한 수가 이미 구한 ans보다 작으면 return (백트래킹)
    if total + ((4 - depth) * max_val) < ans:
        return

    if depth == 4:
        ans = max(ans, total)
        return

    for (dx, dy) in move:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if depth == 2:  # 'ㅗ'모형을 위한 로직
                visited[nx][ny] = True
                dfs(depth+1, total+graph[nx][ny], x, y)
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(depth+1, total+graph[nx][ny], nx, ny)
            visited[nx][ny] = False


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 2차원 배열에서 이동
visited = [[False] * M for _ in range(N)]
ans = -1e9

max_val = max(map(max, graph))

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(1, graph[i][j], i, j)
        visited[i][j] = False

print(ans)
