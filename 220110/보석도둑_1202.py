'''
>> P
보석 N개가 있고 각 M 무게와 V 가격을 갖고있다.
가방 K개가 있고 가방에 담을 수 있는 무게는 C이다
훔칠 수 있는 최대 가격을 구하라
    - 가방에는 최대 한 개의 보석만 넣을 수 있다

>> S
보석과 가방 그리고 최대 가격 -> 그리디 알고리즘

>> 전략
범위가 크고 시간 제한이 1초 => O(n**2)부터 시간초과 남

가방을 작은 것부터 채워가는데 해당 용량보다 작은 것 중 비용이 가장 비싼거 담아
그다음 기방 용량과 용량보다 작은 것 중 가장 비용 큰 것 추리고

1. 가방과 보석을 다른 변수에 담는다
2. 가방을 정렬 후 용량이 작은 값부터 꺼낸다.
3. 가방 용량보다 가벼운 보석 중 비싼 값을 꺼낸다.
    - 1) heapq로 꺼내면 시간 복잡도가 줄어들까? (무게, 가치)
    - 2) 상황에 맞춰 추린 후 정렬 & pop() -> 정렬은 O(nlogn)이니까 
        -> 무게에 따로 추리는게?? 
            -> dict 사용하는건? {'무게':[비용들]}
                -> 만약 가방무게가 2라면 0~1를 접근해서 [0][1] 중 큰 값을 뽑고 해당 값을 del[]
4. 2번~3번 반복


>> 다른 문제 풀이 보고

와 우선순위 큐 사용하는 문제 맞았어!!!
Max-heap 형태로 문제를 해결했는데
1. 가방, 보석 모두 오름차순 정렬
2. 가방 반복문 
    - for capa in bag:
3. jewel이 있고 가방 무게보다 작거나 같으면 해당 가치를 - 붙여(max-heap) prioriity_queue에 담아
    if jewel and capa >= jewel[0][0]:
        heapq.heappush(temp, -jewel[0][1])
        healq.heappop(jewel)    # 작은 값이 먼저 나가는데 오름차순 정렬이니까 맨 앞(작은) 값이 빠져나가
4. temp에 값이 있으면 해당 값을 추가
5. temp에 없고 jewellist에도 값이 없으면(== 가방 용량에 따라 temp에 다시 추가될 수 ㅣㅇㅆ어)
    break
'''
# from collections import defaultdict
# import sys

# input = sys.stdin.readline


# def solve():
#     global jewel
#     ret = 0

#     while bag:
#         capa = bag.pop()
#         prev = 0

#         for key in sorted(jewel.keys()):
#             if key > capa:
#                 break

#             if not jewel[key]:
#                 continue

#             maxv = jewel[key].pop()
#             if prev < maxv:
#                 prev = maxv
#                 continue
#             jewel[key].append(maxv)

#         ret += prev

#     return ret


# N, K = map(int, input().split())
# jewel = defaultdict(list)

# for _ in range(N):
#     m, v = map(int, input().split())
#     jewel[m].append(v)
# bag = [int(input().rstrip()) for _ in range(K)]

# for key in jewel.keys():
#     jewel[key].sort()

# bag.sort(reverse=True)

# ans = solve()

# print(ans)

import sys
import heapq


def solve():
    global jewelry
    ret = 0

    temp = []
    for capa in bag:
        while jewelry and jewelry[0][0] <= capa:    # 보석이 있고 무게가 용량보다 작은동안 반복
            heapq.heappush(temp, -jewelry[0][1])    # -붙여서 MAX-HEAP 만듦
            heapq.heappop(jewelry)

        if temp:    # 가방마다 보석 1개니까 1번만 수행
            ret += heapq.heappop(temp)  # 갖고갈 수 있는 보석 중 가장 가치가 큰 것
        elif not jewelry:
            break

    return -1 * ret


N, K = map(int, input().split())
jewelry = [tuple(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]

# 오름차순 정렬
jewelry.sort()
bag.sort()

ans = solve()

print(ans)
