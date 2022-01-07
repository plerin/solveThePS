'''
>> P
N개의 회의의 시작/끝 시간이 주어졌을 때 중복없이 회의할 수 있는 최대 횟수 구하라
    - 회의가 끝나는 시간에 다음 회의가 시작될 수 있음
    - 회의 시작과 끝 시간이 같을 수 있음
>> S
주어진 조건에서 최대의 효율을 뽑아내야해 --> 그리디
dfs() + 재귀로 풀어보자 
    bc : start가 max보다 크거나 같은경우
입력을 노드 그리고 단방향이라고 따져 
전략
1. 회의 시작 시간 순으로 정렬
2. 

def solve(start: int, cnt: int):
    global ans, visited
    if start >= MAX:
        ans = max(ans, cnt)
    
    for i in range(start, MAX):
        # if not arr[i]:
        #     continue
        for v in arr[i]:
            arr[i].remove(v)
            dfs(v, cnt+1)
            arr[i].add(v)
'''
from collections import defaultdict
import sys
input = sys.stdin.readline


def solve(start: int, cnt: int):
    global ans, visited
    if start >= maximum:
        ans = max(ans, cnt)
        return

    for i in range(start, maximum+1):
        for v in meeting[i]:
            meeting[i].remove(v)
            solve(v, cnt+1)
            meeting[i].append(v)


N = int(input())
# meeting = defaultdict(list)
maximum = 0
# for i in range(N):
#     start, end = map(int, input().split())
#     meeting[start].append(end)
#     maximum = max(maximum, start)
# {list(map(int, input().split())) for _ in range(N)]
# meeting = [list(map(int, input().split())) for _ in range(N)]
# print(sorted(meeting))
# meeting.sort
ans = 0
meeting = []
for i in range(N):
    s, e = map(int, input().split())
    meeting.append((e-s, s, e))
    maximum = max(maximum, e)

meeting.sort(reverse=True)
visited = [False] * (maximum+1)
# print(visited)
while meeting:
    time, s, e = meeting.pop()
    # print(s, e)
    if visited[s] == False and visited[e] == False:
        ans += 1
        for i in range(s, e+1):
            visited[i] = True
# for i in range()
print(ans)

# solve(0, 0)

# print(ans)
