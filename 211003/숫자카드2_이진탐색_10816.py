'''
goal : N개의 숫자카드를 갖고 있을 때 M개의 정수가 적혀있는 각 숫자카드의 개수를 출력
아이디어 : N,M의 범위가 10만이상 + 검색 => 이진탐색 => 정렬필요
0. 라이브러리 추가 - sys: 입력, bisect : 이진탐색 
1. 입력 받기 
    1) N : 숫자카드(정렬필요), M : 정수 모음
2. M를 루프 돌며 각 요소마다 개수 확인 함수 호출
    1) 함수 -> bisect_left/right를 통해 가장 왼쪽/오른쪽 인덱스를 통해 개수 확인
3. 결과 출력
'''
# 0
from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline


def count_by_value(elem):
    left_idx = bisect_left(num_card, elem)
    right_idx = bisect_right(num_card, elem)
    return right_idx - left_idx


# 1
n = int(input())
num_card = sorted(map(int, input().split()))
m = int(input())
num_lst = list(map(int, input().split()))

# 2
ret = []
for e in num_lst:
    ret.append(count_by_value(e))

# 3
print(*ret, sep=' ')
