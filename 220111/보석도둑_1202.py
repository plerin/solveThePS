'''
>> P
보석이 N개가 있는데 무게는 M, 가격은 V이다
가방이 K개가 있고 최대 용량은 K이다
훔칠 수 있는 보석의 최대 가격을 구하시오
    - 가방은 최대 1개의 보석만 담을 수 있다.
>> S
가방과 보석이 있고 최대 가격 구하라 ==> 탐욕적이다 == 그리디

>> 전략
우선순위 큐 향기가 가득.. 조건에 맞는 경우를 모두 우선순위 큐에 넣어두고 그 중에서 꺼내서 사용하도록 하기
1. 가방 용량이 작은 순서대로 반복하며 무개가 용량보다 작은 경우를 추려(우선 순위 큐에 담아)
2. 약탈할 수 있는 보석 중 가치가 가장 큰 보석(우선순위 사용)을 리턴 변수에 더해줘
>> 정리
1. 가방 용량보다 무게가 가볍거나 같은 보석을 우선순위 큐에 담는다.
2. 우선순위 큐에 있는 보석을 꺼내어 리턴 변수에 합한다.
3. 1번과 2번을 반복한다.
    - 가방의 개수만큼만 반복.
>> 코드
1. 보석과 가방 모두 오름차순 정렬
2. 함수 호출
def steal_jewelry():
    global jewelry, bag
    ret = 0
    tmp = []
    while bag:
        capa = bag.pop() # bag는 내림차순 정렬하자
        if jewelry and jewelry[0][0] <= capa:
            heapq.heappush(tmp, -jewelry[0][1])
            heapq.heappop(jewelry)

        if tmp:
            ret += heapq.heappop(tmp)
        elif not jewelry:
            break
    return ret 
'''
import sys
import heapq

input = sys.stdin.readline


def steal_jewelry() -> int:
    global jewelry, bag
    ret = 0
    tmp = []

    while bag:  # 가방에 최대 보석 담는 개수 1개
        capa = bag.pop()    # 용량이 작은 것부터
        while jewelry and jewelry[0][0] <= capa:    # 보석 무게가 용량보다 작을 때까지
            heapq.heappush(tmp, -jewelry[0][1])  # max-heap 구현위해 '-'를 붙여줌
            heapq.heappop(jewelry)  # 가장 작은 값([0][0])을 제거

        if tmp:
            ret += heapq.heappop(tmp)
        elif not jewelry:
            break

    return ret * (-1)


N, K = map(int, input().split())
jewelry = [tuple(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]

jewelry.sort()
bag.sort(reverse=True)  # 가벼운 용량부터 pop()하기 위함

ans = steal_jewelry()

print(ans)
