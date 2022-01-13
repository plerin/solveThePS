'''
>> P
N개의 원소가 오름차순 정렬된 수열에서 x가 등장하는 횟수를 구하라 
    - 시간 복잡도 O(logN)으로 설계하라
    - 범위 : 개수 - ~ 100만, 원소 -10억 ~ 10억
>> S
정렬 & 큰 범위 == 이진탐색을 바로 떠올려라

'''
from bisect import bisect_left, bisect_right


def solve() -> int:
    left_idx = bisect_left(seq, x)
    right_idx = bisect_right(seq, x)

    return right_idx - left_idx


N, x = map(int, input().split())
seq = list(map(int, input().split()))

ans = solve()

print(ans) if ans != 0 else print(-1)
