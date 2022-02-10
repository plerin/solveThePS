'''
>> P
N개의 대학에서 강연을 신청했는데 d일안에 오면 P만큼에 보수를 주겠다고 한다.
벌 수 있는 가장 많은 보수를 구하라
    - 하루에 최대 한 곳에서만 강연 가능
>> S
해당 일자에 가장 보수가 큰 곳을 방문하면 됨(그리디)
간과했던 부분이 일자에 따라 최대 보수 1개씩 방문했는데
    -1일 1개 보수 10 , 3일 3개 보수 40,50,60 이면 1일자 방문할 필요없이 3일꺼 3개 모두 방문하면됨
1일인경우 1일 이상인것만 할 수 있어
2일인경우 2일이상인것만 할 수 있어
3일인경우 3일이상인 것만 할 수 있어

와!
거꾸로가자 d를 내림차순으로 탐색하며 해당 범위에서 선택할 수 있는 값중 가장 큰값 
5
10 1
40 3
50 3
60 3
5 10
위와 같이 주어졌을 경우
10 - 3 - 3 - 3 - 1 순서대로 내림차순 탐색
10부터 1까지 반복
9보다 작은 값이 없으면 continue
10이 있으면 빼버려

>> C
1. 입력 값 변수에 저장
    - 가장 큰 d를 저장
n = int(input())
proposal = [tuple(map(int, input().split())) for _ in range(n)]
max_day = max([day for price, day in proposal])

2. 함수 호출
ans = solve()

def solve():
    temp = []
    ret = 0
    for day in range(max_day,0,-1):
        if not proposal[day]:
            continue
        while proposal and proposal[0][0] == day:
            heapq.heappush(temp, proposal[0][1])
            heapq.heappop(proposal)
        
        if temp:
            ret += heapq.heappop(temp)
        elif proposal:
            break

    return ret


'''
import sys
import heapq

input = sys.stdin.readline


def solve() -> int:
    global proposal
    heap = []
    ret = 0

    for day in range(max_day, 0, -1):  # max_day -> 1
        while proposal and proposal[0][0] == day:   # 해당 일자의 값이 있다면
            heapq.heappush(heap, -1 * proposal[0][1])   # max-heap 구하기 위함
            proposal.pop(0)

        if heap:
            ret += heapq.heappop(heap)
        elif not proposal:
            break

    return ret * (-1)   # max-heap으로 구했으므로


n = int(input())
proposal = []
max_day = 0  # 최대 일자(d)를 구함

for _ in range(n):
    price, day = tuple(map(int, input().split()))
    proposal.append((day, price))   # (p, d) -> (d, p)로 변경
    max_day = max(max_day, day)

proposal.sort(reverse=True)  # 내림차순 탐색을 위한 역정렬

ans = solve()

print(ans)
