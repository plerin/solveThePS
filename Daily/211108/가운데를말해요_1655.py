'''
>P
정수를 하나씩 말할 때마다 중간 값을 말하는 프로그램 작성
    - 외친 수의 개수가 짝수개라면 중간에 있는 두 수중 작은 수를 선택
>S
시간 제한이 0.6초
정수 범위가 1~10만
입력 하나씩 리스트에 입력 & 정렬 후 홀수/짝수에 따라 계산 후 리턴해주면 될까?
    - 개수 1인 경우 : 그대로 반환
    - 개수 홀수 인 경우 : LEN(ARR)//2
    - 짝수 인 경우 : LEN(ARR)//2 - 1
'''

import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
# left = 기준 값보다 작은 값, right = 큰 값
left_arr, right_arr = [], []

for i in range(1, N+1):
    num = int(input().rstrip())

    if len(left_arr) <= len(right_arr):
        # left가 최대힙을 사용하는 이유 : 작은 수중 가장 큰 값이 중간값이 되기 때문에 최대 힙 사용
        heapq.heappush(left_arr, (-num, num))
    else:
        heapq.heappush(right_arr, (num, num))

    if right_arr and (left_arr[0][1] > right_arr[0][1]):
        left_num = heapq.heappop(left_arr)[1]
        right_num = heapq.heappop(right_arr)[1]
        heapq.heappush(right_arr, (left_num, left_num))
        heapq.heappush(left_arr, (-right_num, right_num))

    print(left_arr[0][1])
