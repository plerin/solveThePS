'''
>> P
N개 직사각형 모양 건물들이 주어질 때 스카이라인(건물의 윤곽)을 구하라
    - 직사각형들의 합집합
    - 범위 = 개수 : < 10만 / 값 : ~ 10억

>> S
1. 우선순위 큐, 정렬, set 키워드를 뽑아내는 것이 첫번째 목표
2. 규칙을 찾아내는 것
3. 코드로 작성하는 것 

(다른 사람의) 접근
1. 스카이라인의 외각점은 갑자기 높이 상승한 지점과 갑자기 높이가 하강한 지점으로 이루어져 있다.
    - 하강한 지점은 2가지로 나뉘는데 남은 건물 중 가장 높은 지점과 남은 건물이 없는경우(0)
    -> 우선순위가 필요하므로 우선순위 큐를 사용
2. 시작점과 끝점이 동일 지점에 존재할 경우
    - 시작점을 끝점보다 우선시 계산해야 함(안그럼 더 높은 지점이 있음에도 0이됨)
    -> 시간지점을 끝지점보다 우선시 정렬
3. 시작지점이 동일한 여러 건물이 있는 경우
    -> 더 높은 시작점을 우선시 한다
4. 끝지점이 동일한 여러 건물 있는 경우
    -> 건물이 끝나는 시점도 저장하여 풀이함

'''

import sys
import heapq

input = sys.stdin.readline

# 입력
n = int(input())
arr = []
height = [0] * n
q = []

end = [0] * n
check = set()

for i in range(n):
    a, b, c = map(int, input().split())

    arr.append((a, i, 1))
    arr.append((c, i, -1))
    height[i] = b
    end[i] = c

# 우선순위 1. 시점, 2. 시작점, 3. 높이 높은지
arr.sort(key=lambda x: (x[0], -x[2], -height[x[1]]))

# now : 현재 최고 높이
now = 0
ans = []
for i in range(len(arr)):
    # point : 시점, idx : 건물 순서, dir : 시작점 / 끝점 여부
    point, idx, dir = arr[i]

    if dir == 1:
        if now < height[idx]:
            now = height[idx]
            ans.append((point, now))
        # 높이 갱신됨과 상관없이 현재 건물 높이와 끝점을 최대 힙에 저장
        heapq.heappush(q, (-height[idx], end[idx]))
    else:
        # 현재 시점이 끝났기 때문에 set에 끝점의 시점을 저장
        check.add(point)
        # 최대 높이가 끝난 건물이 아닐때까지 pop
        while q:
            if q[0][1] not in check:
                break
            heapq.heappop(q)
        # 힙이 비었다면 스카이라인의 높이는 0으로 갱신
        if not q:
            if now:
                now = 0
                ans.append((point, now))

        # 힙이 있다면 현재 높이와 비교시 변동이 있다면 그 높이가 그 다음 높은 건물이기 때문에 높이 갱신
        else:
            if -q[0][0] != now:
                now = -q[0][0]
                ans.append((point, now))

for i in ans:
    print(i[0], i[1], end=' ')
