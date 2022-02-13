'''
backjoon url -> https://www.acmicpc.net/problem/1931

>> Keyword
그리디(끝나는 시간 중 작은 값을 먼저 처리), heapq(작은 값을 먼저 처리하기 위함)

>> P
한 개의 회의실이 있고 이를 사용하는 N개의 회의가 주어진다.
시작 시간, 끝나는 시간이 같이 주어질 때 겹치지 않고 회의 가능한 최대 개수를 횟수 구하라
    - 끝나는 동시에 회의 시작할 수 있다

>> S
주어진 규칙에서 최대 개수를 찾아야 해 
가장 효율적인 방법을 찾아보자
=> 그리디

접근
끝나는 시간을 기준으로 오름차순 정렬
1. 끝나는 시간이 가장 작은 값 추출
2. 1번 결과보다 작은 값 제외 
1,2번을 반복진행하며 cnt += 1

정당성 검증
끝나는 시간 기준으로 오름차순 정렬하면 다음 회의를 찾을 수 있음

코딩
1. heapq 선언 하고 회의 시간을 입력 
meeting = []
heapq.heappush(meeting, (end, start))
2. 리턴 값 선언(0) 현재 시간(now) 선언(0)
ret = now = 0
3. 회의 시간 리스트가 빌 때까지 반복 하며 now,ret 갱신하고 now보다 작은 시작시간은 pass
while meeting:
    end, start = heapq.heappop(meeting)
    if now < start:
        now = end
        ret += 1
'''

import heapq
import sys

input = sys.stdin.readline


def assign_room(meeting: list) -> int:
    ret = now = 0

    while meeting:
        end, start = heapq.heappop(meeting)
        if now <= start:
            now = end
            ret += 1

    return ret


N = int(input())
meeting = []

for _ in range(N):
    start, end = map(int, input().split())
    heapq.heappush(meeting, (end, start))

print(assign_room(meeting))


input = sys.stdin.readline

N = int(input())
arr = sorted([tuple(map(int, input().split()))
              for _ in range(N)], key=lambda x: (x[1], x[0]))
ans = end = 0
for s, e in arr:
    if s >= end:
        ans += 1
        end = e

print(ans)
