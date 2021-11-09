import sys
import heapq

input = sys.stdin.readline

coords = []

for _ in range(int(input())):
    x, y = map(int, input().split())
    heapq.heappush(coords, (y, x))

while coords:
    y, x = heapq.heappop(coords)
    print(x, y)
