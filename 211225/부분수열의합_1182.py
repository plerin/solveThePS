'''
>> P
N개 정수로 이루어진 수열이 있을 때 S를 만드는 부분 수열 개수 구하라
    - 수열의 원소의 합이 S인 부분수열
>> S
1. 라이브러리 활용 방법(combination)
    - combination으로 1 ~ N 개수를 사용한 부분 집합 중 합을 구하기
2. 재귀 풀이 방법(dfs)
    - 순서가 바뀌지 않도록 함 -> -7, -3과 -3과 -7의 결과(합)은 같아
        -> param에 start와 반복 range에 start를 지정
>> F
def dfs(start: int):
    - vari : visited(list) _ size는 N로 갖고 0으로 초기화 갱신하면 값을 갖음
    - logic
        1) bc는 없고 더이상 탐색 못하면 return
        2) 탐색할 때 True 처리하고 재귀타고 False하기 전에 값 갱신
'''

from itertools import combinations
import sys
sys.setrecursionlimit(10**8)


def use_library(num: int):
    global ans

    for i in range(1, num+1):
        for case in combinations(seq, i):
            if sum(case) == S:
                ans += 1


# def dfs(start: int):
#     global visited, ans

#     for i in range(start, N):
#         if visited[i]:
#             continue
#         visited[i] = str(seq[i])
#         dfs(i)

#         if sum(map(int, visited)) == S:
#             ans += 1

#         visited[i] = 0

#     return

def dfs(idx: int, sum: int):
    global ans
    if idx >= N:
        return

    sum += seq[idx]
    if sum == S:
        ans += 1
    dfs(idx + 1, sum - seq[idx])    # 해당 값을 포함하지 않는 경우
    dfs(idx + 1, sum)   # 해당 값을 포함한 경우


N, S = map(int, input().split())
seq = list(map(int, input().split()))
visited = [0] * N  # 방문 여부 체크
ans = 0

dfs(0, 0)
# use_library(N)

print(ans)
