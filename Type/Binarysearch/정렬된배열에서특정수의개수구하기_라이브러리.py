'''
youtube url -> https://www.youtube.com/watch?v=94RC-DsGMLo

>> Keyword
오름차순 정렬 & 시간 복잡도 O(logN) => 이진탐색

>> P
N개의 원소를 포함하는 수열이 오름차순 정렬되어 있을 때
수열에서 x가 등장하는 횟수 계산
    - 단 시간복잡도 O(logN)으로 설계해야 함

>> S
보자마자 '정렬된 수열'에서 '시간복잡도 O(logN)'에서 이진 탐색임을 확인

접근
1. 라이브러리 활용
금방 끝나 bisect_right() - bisect_left()

'''

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline


def count_number(seq, target):
    right_idx = bisect_right(seq, target)
    left_idx = bisect_left(seq, target)

    return right_idx - left_idx if right_idx != left_idx else -1


N, x = map(int, input().split())
seq = list(map(int, input().split()))

print(count_number(seq, x))
