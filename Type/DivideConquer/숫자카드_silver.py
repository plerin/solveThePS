'''
backjoon url -> https://www.acmicpc.net/problem/10815

>> Keyword
이진탐색, 
>> P
숫자카드는 정수가 하나씩 적혀있다.
상근이가 N개의 숫자카드를 갖고있고 정수 M개가 주어졌을 대 상근이가 갖고있는지 판단하기
    - 범위 -> N,M ~ 50만, 값의 범위 -1000만 ~ 1000만

>> S
일반 선형탐색으로 진행하면 시간초과 나올 범위
이진탐색 또는 분할정복 풀이 방법 찾아보기

이진탐색 풀이
1. N의 숫자를 정렬함(오름차순)
2. 이진탐색 라이브러리 활용해서 bisect_right - bisect_left 한 값이 0이면 0 그 이상이면 1 출력 

-> 시간복잡도 O(NlogN)예상

분할정복 풀이



'''

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline


def is_there(target):
    idx_left = bisect_left(card, target)
    idx_right = bisect_right(card, target)

    return 0 if idx_left == idx_right else 1


n = map(int, input().rstrip())
card = list(map(int, input().split()))
m = int(input().rstrip())
num = list(map(int, input().split()))

ans = []

card.sort()

for val in num:
    ans.append(is_there(val))

print(*ans, sep=' ')
