'''

이진 탐색

>> 라이브러리
from bisect import bisect_left, bisect_right

bisect_left(a, x) : 정렬된 순서를 유지하며 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
bisect_right(b, x) : 정렬된 순서를 유지하며 배열 b에 x를 삽입할 가장 오른쪽 인덱스 반환
'''


# 라이브러리 활용
from bisect import bisect_left, bisect_right


def count_by_range(arr, left, right):
    right_idx = bisect_right(arr, right)
    left_idx = bisect_left(arr, left)
    return right_idx - left_idx


arr = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(arr, 4, 4))

print(count_by_range(arr, -1, 3))
