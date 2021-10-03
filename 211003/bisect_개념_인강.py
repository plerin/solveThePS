

from bisect import bisect_left, bisect_right


def count_by_range(arr, left_v, right_v):
    right_idx = bisect_right(arr, right_v)
    left_idx = bisect_left(arr, left_v)
    return right_idx-left_idx


arr = [1, 2, 3, 3, 3, 3, 4, 5, 6]

print(count_by_range(arr, 4, 4))

print(count_by_range(arr, -1, 5))
