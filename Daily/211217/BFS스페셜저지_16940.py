'''
>> P
정점이 1~N인 양방향 그래프가 있고 트리가 주어졌을 때 올바른 BFS 방문 순서 여부 확인
    - 시작 정점은 1
    - 방문 순서에 따라 여러가지 결과가 나올 수 있다.
>> S
주어진 그래프로 BFS를 구하면 항상 같은 트리만 나와
    -> 주어진 트리에 맞도록 순서를 바꿔서 BFS 출력해야해
    -> 트리의 값과 인덱스로 우선순위 정렬 수행
1. 트리의 값과 인덱스로 우선순위 리스트 생성
2. 우선순위 리스트로 GRAPH의 값 정렬
3. GRAPH의 BFS 구하기
4. 트리와 비교하기
'''

from collections import deque


def bfs(start: int):
    queue = deque([start])
    visit[start] = True

    while queue:
        v = queue.popleft()
        ans.append(v)
        for i in graph[v]:
            if visit[i]:
                continue
            visit[i] = True
            queue.append(i)


N = int(input())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)
order = [0] * (N+1)

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

tree = list(map(int, input().split()))
ans = []

for idx in range(len(tree)):
    order[tree[idx]] = idx

for i in range(len(graph)):
    graph[i].sort(key=lambda x: order[x])

bfs(1)

if ans == tree:
    print(1)
else:
    print(0)
