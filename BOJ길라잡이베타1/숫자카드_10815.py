'''
>P
N개의 숫자 카드를 갖고 있는데 M개의 숫자 카드 중 갖고 있는 여부 판단 프로그램 작성
    - 갖고 있으면 1 아니면 0
>S
구현문제
카드 개수 범위가 50만 , 카드 정수는 -천만~+천만  -> 시간 복잡도가 크지 않도록 풀이
1. N과 M을 모두 우선순위 큐에 담아놓고 풀이하는건?  -> 아니야 M은 들어온 순서대로 계산해
2. 범위가 클 때 생각할 수 있는 게 이진탐색 
    - 준비물 : 라이브러리(bisect) // 정렬
'''
from bisect import bisect_left, bisect_right


def binarySearch1(n):
    left_idx = bisect_left(n_arr, i)
    right_idx = bisect_right(n_arr, i)

    if right_idx-left_idx == 0:
        print(0, end=' ')
    else:
        print(1, end=' ')


def binarySearch2(target, start, end):
    global n_arr
    global m_arr
    while start <= end:
        mid = (start+end) // 2

        if target == n_arr[mid]:
            return True
        elif n_arr[mid] < target:
            start = mid+1
        else:
            end = mid-1

    return False


N = int(input())
n_arr = list(map(int, input().split()))
M = int(input())
m_arr = list(map(int, input().split()))

n_arr.sort()

for i in m_arr:
    # binarySearch1(i)
    start, end = 0, len(n_arr)-1
    ret = binarySearch2(i, start, end)
    if ret == False:
        print(0, end=' ')
    else:
        print(1, end=' ')
