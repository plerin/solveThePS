'''
순차 탐색 = 1부터 N까지 순차적으로 확인하는 방법  
    - 시간 복잡도 : O(N)
이진 탐색 = 탐색 범위를 절반으로 줄여가며 탐색하는 방법 
    - left / right/ mid 를 사용
    - 시간 복잡도 : O(logN) ==> 탐색할 때마다 범위를 줄이기 때문에
    - 전제 조건 : 정렬이 되어있어야 함 & 범위가 큰 경우 주로 사용

라이브러리
from bisect

bisect_left(a, x) : 정렬된 순서를 유지하며 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
bisect_right(a, x) : 정렬된 순서를 유지하며 배열에 x를 삽입할 가장 오른쪽 인덱스 반환

arr = [1 3 5 7 11 11 11 17 19]
ex) bisect_left(arr, 11) = 4 // bisect_right(arr, 11) = 7

파라메트릭 서치
최적화 문제를 결정 문제로 바꾸어 해결하는 기법
    ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
    

10 7
1 3 5 7 11 13 15 17 19

10 7
1 3 5 8 11 13 15 17 19



'''
from bisect import bisect_left, bisect_right

arr = [1, 3, 5, 7, 11, 11, 11, 17, 19]
l = bisect_left(arr, 11)
r = bisect_right(arr, 11)
print(l, r)


def bisect_recursive(left: int, right: int) -> int:
    if left > right:
        return None

    ret = None
    mid = (left + right) // 2

    if arr[mid] < target:
        ret = bisect_recursive(mid+1, right)
    elif arr[mid] > target:
        ret = bisect_recursive(left, mid-1)
    else:
        return mid

    return ret


def bisect_loop(left: int, right: int) -> int:

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid

    return None


# # n개 수열에서 target 순서를 찾는 문제(없으면 없다고 출력)
# n, target = tuple(map(int, input().split()))
# arr = list(map(int, input().split()))

# left, right = 0, len(arr) - 1

# # ans = bisect_recursive(left, right)
# ans = bisect_loop(left, right)

# # index를 반환하기 때문에 + 1
# print(ans+1) if ans != None else print('원소가 존재하지 않습니다.')
