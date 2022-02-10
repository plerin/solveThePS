'''
>> P
직사각형들의 윤곽(스카이라인)을 구하라
    - 범위 : 개수 : ~ 10만, 값 : ~10억
>> S
접근
1. 스카이라인의 경계가 되는 지점(상승/하강)을 구해야 한다
2. 시작점과 끝점으로 정렬
3. 시작점과 끝점이 같은 지점이라면 시작점을 우선해야 함
4. 같은 시작점으리면 더 높은 건물이 우선순위
5. 끝점이 같다면 다음 높은 높이가 이미 끝난 지점의 높이인지 판단
'''

import sys
import heapq

input = sys.stdin.readline

# 입력부
n = int(input())
arr = []
height = [0] * n
q = []

# 현재 index번째 건물의 끝나는 지점 저장
end = [0] * n
# 현재까지 끝난 끝점을 저장하는 set(끝점에서 다음 끝나지 않은 건물 높이 있는지 확인)
check = set()

for i in range(n):
    a, b, c = map(int, input().split())
    # 시작점이면 1, 끝점이면 -1
    arr.append((a, i, 1))
    arr.append((c, i, -1))
    height[i] = b
    end[i] = c

# 정렬 기준
# 1. 시점이 앞서는지(출발점/끝점) 2. 시점이 같다면 시작점인지 끝점인지 3. 시점이 같고 시작점인 경우 높은 경우
arr.sort(key=lambda x: (x[0], -x[2], -height[x[1]]))

# now : 현재 최고높이
now = 0
ans = []
for i in range(len(arr)):
    # 시점, 건물 idx, 시작점/끝점
    point, idx, dir = arr[i]

    if dir == 1:
        # 높이가 갱신된다면 새로운 스카이라인 윤곽
        if now < height[idx]:
            now = height[idx]
            ans.append((point, now))
            # 높이 갱신 상관 없이 현재 건물 높이와 끝점을 최대 힙에 저장
        heapq.heappush(q, (-height[idx], end[idx]))
    else:
        # 현재 시점이 끝났기 때문에 set에 끝점 시점 저장
        check.add(point)

        # 최대 높이가 끝난 건물이 아닐때까지
        while q:
            if q[0][1] not in check:
                break
            heapq.heappop(q)

        # 힙이 비었다면 높이는 0으로 갱신
        if not q:
            if now:
                now = 0
                ans.append((point, now))
        else:
            if -q[0][0] != now:
                now = -q[0][0]
                ans.append((point, now))

for i in ans:
    print(i[0], i[1], end=' ')
