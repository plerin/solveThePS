'''
>> P
n개 대학에서 강연요청을 했다.
d일 안에 오면 P만큼 수강료 지불한다고 할 때
최대로 벌 수 있는 돈을 출력하라
    - 하루에 최대 한 곳만 강연 가능 
>> S
제한-소득 이 주어지고 이 중 가장 많이 벌 수 있는 경우 == 그리디

>> 전략
우선순위 큐가 보고싶네
d를 오름차순으로 뽑으며 해당 d의 가장 큰 값만을 더해주면 풀리겠다
1. 입력 값을 우선순위 큐에 담아
2. while로 반복하며 d 중 가장 큰 값을 더하기
dictionary로 풀이 가능
1. defaultdict(list) 생성
2. [d].append(p)
3. key()를 반복하며 max()값 더해줘 // key() 정렬 후 pop으로 뽑기

>> 코드
1. 
schedule = defaultdict(list)
schedule[d].append(p)
2.
for key in schedule.keys():
    schedule[key].sort()
3.
ret = 0
for key in schedule.keys():
    max_price = schedule[key].pop()
    ret += max_price
4. return

'''
import sys
from collections import defaultdict

input = sys.stdin.readline


def solve() -> int:
    global schedule
    ret = 0
    print(schedule.keys())
    for key in schedule.keys():
        max_price = sorted(schedule[key]).pop()  # 해당 key에서 가장 큰 값 반환
        ret += max_price

    return ret


n = int(input())
schedule = defaultdict(list)    # 기본 값 []으로 갱신
for _ in range(n):
    p, d = map(int, input().split())
    schedule[d].append(p)

ans = solve()

print(ans)
