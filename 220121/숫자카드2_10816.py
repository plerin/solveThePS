'''
>> P
숫자 카드 N개가 있고 정수 M개가 주어졌을 때
M에 대해 갖고있는 숫자 카드 개수를 구하라 
    - 범위 -> 개수 : ~50만 // 값 : -1000만 ~ 1000만
>> S
어떤 문제 유형이든 범위가 큰 경우 완전 탐색 O(N**2)은 불가능 -> O(NlogN) 알고리즘 활용
이분탐색으로 풀어보자

접근
    1) 오히려 더 쉬운게 bisect 라이브러리 활용해서 bisect_right() - bisect_left() 값을 입력
'''

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline


def get_num() -> None:
    card_n.sort()   # 이분탐색 하기 전 전제조건인 정렬 수행

    for num in card_m:
        idx_left = bisect_left(card_n, num)
        idx_right = bisect_right(card_n, num)

        print(idx_right-idx_left, end=' ')


cnt_n = int(input())
card_n = list(map(int, input().split()))
cnt_m = int(input())
card_m = list(map(int, input().split()))

get_num()
