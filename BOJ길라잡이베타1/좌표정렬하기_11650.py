'''
> P
2차원 평면 위 N개의 점을 정렬하라
    - x좌표 오름차순 -> 같으면 y좌표 오름차순
> S
유형 : 구현
튜플로 묶고 sorted(key=lambda x: (x[0],x[1]))
'''

import sys
import heapq

input = sys.stdin.readline

N = int(input())
coords = []

for _ in range(N):
    x, y = map(int, input().split())
    heapq.heappush(coords, (x, y))

while coords:
    print(*heapq.heappop(coords))

# coords.sort(key=lambda x: (x[0], x[1]))

# for x, y in coords:
#     print(x, y)

# print(*sorted(coords, key=lambda x: (x[0], x[1])), sep='\n')
