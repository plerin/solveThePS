'''

이진 탐색

>> Concept

순차탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 확인하는 방법
이진탐색 : '정렬'되어있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색
    - 시작점(start), 끝점(end), 중간점(mid)

이분탐색 -> 무엇을 탐색할 것인지가 가장 중요!

필요 조건
- 정렬된 리스트

시간복잡도
- O(logN)

라이브러리
from bisect import bisect_left, bisect_right

bisect_left(a, x) : 정렬된 순서를 유지하며 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
bisect_right(b, x) : 정렬된 순서를 유지하며 배열 b에 x를 삽입할 가장 오른쪽 인덱스 반환
'''

# 재귀


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)

# 반복


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            end = mid - 1
        elif array[mid] > target:
            start = mid + 1

    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)


# 라이브러리 활용
#from bisect import bisect_left, bisect_right

def count_by_range(arr, left, right):
    right_idx = bisect_right(arr, right)
    left_idx = bisect_left(arr, left)
    return right_idx - left_idx


arr = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(arr, 4, 4))

print(count_by_range(arr, -1, 3))
