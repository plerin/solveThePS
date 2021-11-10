'''
[P]
N개의 정수 안에 정수 X가 존재하는 알아내는 프로그램

[S]
N,M의 최대 범위는 100,000이고 이를 O(N**2)으로 풀면 시간초과
    - 유형 : 이진탐색 그중 표준 라이브러리 사용하기
[L]
1. 이진 탐색 준비물
    - 라이브러리 _ from bisect
2. 입력 받기
    - N(int) : 개수 , n_arr(list)
    - M(int) : 정수 개수, m_arr(list) 
3. m_arr를 반복하며 bisect_left/right 가 0이면  0 출력 아니면 1 출력
'''

import sys

input = sys.stdin.readline


def binary_search(target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if n_arr[mid] == target:
            return mid
        elif n_arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


N = int(input())
n_arr = list(map(int, input().split()))
M = int(input())
m_arr = list(map(int, input().split()))

start, end = 0, len(n_arr)-1

n_arr.sort()
for e in m_arr:
    exist = binary_search(e, start, end)
    if exist == -1:
        print(0)
    else:
        print(1)


# from bisect import bisect_left, bisect_right

# N = int(input())
# n_arr = list(map(int, input().split()))

# M = int(input())
# m_arr = list(map(int, input().split()))

# n_arr.sort()
# for e in m_arr:
#     exist = bisect_right(n_arr, e) - bisect_left(n_arr, e)

#     if exist == 0:
#         print(0)
#     else:
#         print(1)
