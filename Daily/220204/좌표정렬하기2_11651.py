'''
>> P
2차원 평면 위 점 N개가 있다
y 증가순, 같으면 x증가순 정렬

>> S
접근
1. heapq 라이브러리 추가
2. 입력 받기 heapq.heappush(arr, (y,x))
3. 출력 
'''

import heapq
import sys

input = sys.stdin.readline


def sort_coord() -> list:
    arr = []
    for _ in range(N):
        x, y = map(int, input().split())
        heapq.heappush(arr, (y, x))

    return arr


N = int(input())
ans = sort_coord()

while ans:
    y, x = heapq.heappop(ans)
    print(x, y)
