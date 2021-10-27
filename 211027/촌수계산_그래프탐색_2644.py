'''
[P]
촌수 계산 _ 두 사람의 촌수를 계산하는 프로그램 작성
    - 부모와 자식간의 촌수는 '1촌'
[S]
BFS를 이용한 촌수 계산 -> 촌수 계산 == 최단 경로
    - BFS를 이용할 수 있는 이유 == 모든 노드 간 비용이 '1촌'으로 같다
[L]
1. 입력 값 변수 선언
    - N(int) : 전체 사람 수 // M(int) : 부모 - 자식 관계 수
    - p1,p2 : int형으로 촌수를 구해야 하는 사람
    - graph(2차원 배열) : 무방향 배열
2. 
'''
from collections import deque


def cal(p1):
    q = deque([p1])
    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v]+1
                q.append(i)


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

visited[p1] = 0

for _ in range(m):
    pa, ch = map(int, input().split())
    graph[pa].append(ch)
    graph[ch].append(pa)

# print(graph)

ret = cal(p1)

print(visited[p2])
