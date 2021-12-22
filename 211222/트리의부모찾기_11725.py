'''
>> P
1이 루트인 트리에서 각 노드 부모 찾기
    - 2번 노드부터 순서대로 출력
>> S
부모 판별 어떻게 하지? 
    - BFS 방식으로 내려가며 연결 노드의 값의 부모를 확정짓고 해당 노드의 연결리스트에 제외
    - 노드를 리스트로 만들고(1~10만) 모두 0으로 채워넣고 부모를 찾으면 값을 넣어주고 0인 것만 갱신해

'''

from collections import deque

MAX = 100001


def find_parent(parent: int):
    global ans

    queue = deque([parent])
    ans[parent] = -1

    while queue:
        parent = queue.popleft()

        for child in graph[parent]:
            if ans[child] != 0:
                continue
            ans[child] = parent
            queue.append(child)


N = int(input())
graph = [[] for _ in range(N+1)]
ans = [0] * (N+1)

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

find_parent(1)

print(*ans[2:], sep="\n")
