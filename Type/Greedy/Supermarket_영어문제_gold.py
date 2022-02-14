'''
backjoon url -> https://www.acmicpc.net/problem/2109

>> Keyword

>> P
물건마다 가격과 마감기한이 주어진다.
각 물건은 하나의 판매 단위가 소요된다. 
주어진 기간동안 최대 수익을 구하라

>> S
수익과 마감기한이 주어질 때 정해진 기간 동안 가장 큰 수익을 구하라
-> 최적의 방법을 찾아 가장 큰 값을 구하라 == 그리디

접근
일자로 탐색하며 가장 큰 값을 입력
- 작을 일자 -> 큰 일자 : 해당 일자가 없을 때 큰 일자를 대신 쓸 수 없어
- 큰 일자 -> 작은일자 : 해당 일자 물건이 없어도 큰 일자를 사용할 수 있어

로직
1. 입력 값 중 데드라인이 가장 큰 값 저장 max_day(int)
2. 탐색 from max_day -> 0 for day in range(max_day, 0, -1)
for price in proc[i].values():
    heapq.heappush(queue, (-price,day)

if not queue:
    continue
else:
    ret += heapq.heappop(queue)

'''
from collections import defaultdict
import sys
import heapq

input = sys.stdin.readline


def get_max_profit(prod: dict) -> int:
    ret = 0
    queue = []
    # 가장 큰 마감일자부터 1일 순서로 반복
    for day in range(max_day, 0, -1):
        # 해당 마감일자를 모두 heapq를 통해 queue에 저장
        for price in prod[day]:
            heapq.heappush(queue, -price)

        if not queue:
            continue
        else:
            # queue가 비어있지 않으면 기존 담아준 값 중에서 가장 비싼 물건 값 더해줌
            ret += heapq.heappop(queue) * -1

    return ret


n = int(input())
# 같은 마감일자의 물건을 담기위한 dict
prod = defaultdict(list)
max_day = 0

for _ in range(n):
    price, deadline = map(int, input().split())
    prod[deadline].append(price)
    max_day = max(max_day, deadline)

print(get_max_profit(prod))
