'''
ref : https://www.daleseo.com/sort-merge/

- 시간 복잡도 : O(NlogN) == split_O(logN) * merge_O(N)
- 공간 복잡도 : O(N) _ 병합 결과를 담을 배열
- 구현 : 재귀
    - 기저조건 : 배열 크기가 2보다 작을 때 -> 배열 반환
    - 로직 : 배열 원소가 하나가 될 때까지 분할 후 병합

'''


def merge_sort(arr):
    # 기저 조건
    if len(arr) < 2:
        return arr

    # split = 배열의 중간을 찾아 절반으로 나눈다
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    # 병합된 배열을 담을 리스트 및 나뉜 리스트 인덱스
    merged_arr = []
    l = h = 0

    # 두 개의 리스트를 돌며 작은 값 입력
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    # 남은 리스트 값 추가
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr


def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:  # 아직 low list에 비교못한 원소가 남아있다면
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
