'''
>> P
N장 카드를 갖고 있고 수는 엄청 클 때 가장 많이 갖고있는 카드를 반환
    - 만약 여러가지면 작은 것 출력

>> S
카운터 사용

접근
1. 입력 받은 값을 Counter 파라미터로 입력
2. most_common(1) 받아오기 
3. 여러개라면 sort해서 첫 번째 값 추출

접근#2
dict활용
1. deafultdict을 만들어주고
2. 입력 받으며 +=1
3. 정렬 후 출력

'''
from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
card = defaultdict(int)
for _ in range(N):
    card[int(input())] += 1

sort_card = sorted(list(card.items()), key=lambda x: (-x[1], x[0]))
print(int(sort_card[0][0]))
