'''
>> P
수열 A가 있을 때 가장 긴 증가하는 부분 수열의 길이를 구하라
    - 개수와 범위가 100만
>> S

가장 긴 증가하는 부분 수열을 구하는 것이 아닌
가장 긴 길이를 구하기 위한 수열 형태를 사용

- 부분수열 마지막 값[-1]보다 크면 append() 작으면 위치를 찾아 변경
    -> 여기서 위치를 찾을 때 시간복잡도 효율화를 위해 이진탐색을 사용
        -> left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if lst[mid] < target:
                left = mid + 1
            elif lst[mid] > target:
                right = mid - 1
            else:
                break
        seq[pos] = target
'''
import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
cases = list(map(int, input().split()))

lst = [0]

# for case in cases:
#     if lst[-1] < case:
#         lst.append(case)
#     else:
#         left, right = 0, len(lst) - 1
#         pos = 0

#         while left <= right:
#             mid = (left + right) // 2

#             if lst[mid] < case:
#                 left = mid + 1
#             elif lst[mid] > case:
#                 right = mid - 1
#             else:
#                 pos = mid
#                 break

#         lst[pos] = case

# 수열을 돌면서 해당 값이 부분 수열에 추가되는지 아니면 위치를 갱신하는지 판단
for case in cases:
    if lst[-1] < case:
        lst.append(case)
    else:
        pos = bisect_left(lst, case)
        lst[pos] = case

print(len(lst)-1)
