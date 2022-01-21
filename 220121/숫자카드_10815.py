'''
>> P
숫자 카드 N개가 있고 카드 M개가 주어질 때 N에 속해있는지 여부 파악
    - 범위 : 카드 개수 ~ 50만, 값 -1000 ~ 1000만
>> S
범위가 클 때 O(N**2)으로 풀면 안됨 다른 방법 이용
이분탐색으로 O(NlogN)으로 풀아보자

접근
    1) 입력 받기 _ 모두 리스트
    2) 함수 호출
    3) M 탐색 -> 이분탐색 -> 있으면 1 append 없으면 0 append 
    4) 리턴 
    5) 출력
'''
from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline


def solve2() -> None:
    arr1.sort()
    for num in arr2:
        left_idx = bisect_left(arr1, num)
        right_idx = bisect_right(arr1, num)

        if right_idx - left_idx == 0:
            print('0', end=' ')
        else:
            print('1', end=' ')


def solve() -> list:
    ret = []

    arr1.sort()  # 이분탐색위한 정렬

    for num in arr2:    # 하나씩 탐색
        left, right = 0, len(arr1) - 1
        pos = 0
        while left <= right:
            mid = (left + right) // 2

            if arr1[mid] < num:
                left = mid + 1
            elif arr1[mid] > num:
                right = mid - 1
            else:
                pos = mid
                break

        if arr1[pos] == num:
            ret.append(1)
        else:
            ret.append(0)

    return ret


n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

solve2()
# print(*solve())
