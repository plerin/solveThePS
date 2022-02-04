'''
>> P
N 수로 이루어진 수열이 있을 때 bubble sort 수행 시 swap 발생 횟수 구하라
    - 개수 범위 : ~ 50만 / 값의 범위 : ~ 10억
>> S
bubble sort를 했을 때 swap 횟수를 구해야하는데 시간복잡도가 O(N^2)이라면 불가능
    - 파이선 1초 연산량 : 2 * 10^7
    - 버블 소트로 계산했을 때 : (5 * 10^5)^2 = 25 * 10^10
-> 다른 정렬 _ 퀵 / 병합 정렬을 통해 풀어야 함


병합정렬 시간 복잡도 O(NlogN) ==> 5*10^5 * log(5*10^5) = 25 * 10^5 => 가능 
병합정렬 = split(O(logN)) * merge(O(N)) 
    1. 배열을 원소가 하나가 될 때까지 나눈다(mid 기준)
    2. 배열 2개를 비교하며 작은 값이 앞 / 큰 값이 뒤로 가도록한 배열을 저장

접근
병합정렬 메소드 생성
param : start, end -> 0, len(arr)을 넣어줌
vari : global cnt
base_condition : if high - low < 2 then return
logic
    1) find the mid using low, high
    2) call recursive by standard mid
    3) create tmp list and l, h index = 0 
    4) compare and insert value in tmp
    5) care of the remaining value 
    6) replace arr with temp

코딩
1. 입력 받기 
import sys

input = sys.stdin.readline
2. 메소드 생성
3. 메소드 호출
'''

import sys

input = sys.stdin.readline


def merge_sort(low: int, high: int) -> None:
    global cnt

    # 원소가 1개가 될 때 재귀 종료
    if high - low < 2:
        return

    mid = (low + high) // 2
    merge_sort(low, mid)
    merge_sort(mid, high)

    # print(low, mid, high)
    tmp = []
    l, h = low, mid

    while l < mid and h < high:
        if arr[l] <= arr[h]:
            tmp.append(arr[l])
            l += 1
        else:
            tmp.append(arr[h])
            h += 1
            # mid-l 인 이유 = a,b 중 b가 사용된다는 건 low 리스트에 남은 값보다 먼저 사용 == 스왑 된다는 의미니까
            cnt += (mid-l)

    while l < mid:
        tmp.append(arr[l])
        l += 1

    while h < high:
        tmp.append(arr[h])
        h += 1

    for i in range(low, high):
        arr[i] = tmp[i - low]
    # print('---->', arr)


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0

    merge_sort(0, N)

    print(cnt)
