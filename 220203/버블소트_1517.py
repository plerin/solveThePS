'''
>> P
N 수로 이루어진 수열이 있을 때 bubble sort 수행 시 swap 발생 횟수 구하라
    - 개수 범위 : ~ 50만 / 값의 범위 : ~ 10억
>> S
일반적인 방법으로 못풀어 범위가 너무 커서
bubble sort에서 swap이 발생하는 경우를 구해보자
1. 앞에서(idx=0)부터 다음 수(idx+1)와 비교하여 앞의 수가 더 크면 swap
2. 수의 개수가 n개라면 n+(n-1)+(n-2)...+1 = O((n*(n+1)//2))

swap
1. 앞이 뒤보다 더 크다
2. 앞이 뒤보다 더 작다 

pattern
숫자가 주어지면 앞에서부터(idx=0) 뒤로 가며 현재 값이 뒤 숫자들보다 큰 경우 횟수의 합
ex) 321 이면 3은 2,1보다 커(2개) + 2는 1보다 커(1개) => swap은 3번 이뤄짐

접근
시간 복잡도 비교
버블 소트 -> n개가 있다면 n-1 + n-2 + n-3 + ... + 1 == n(n-1)/2 == O(N^2)
병합 정렬 -> n개를 절반으로 나누며 1개가 될 때까지 나눠(logn) * 각 원소를 비교하며 새로운 버퍼에 넣는다(=n) == O(nlogn)

n = 50만이라고 하면
python 1초 계산 가능 횟수 = 2 * (10^7)
O(N^2) = (5*(10^5))^2 = 25 * (10^10)
O(NlogN) = 5*(10^5) * log(5*(10^5))

-> 병합정렬 이용해서 시간복잡도 해결하자 


'''
import sys
input = sys.stdin.readline


def mergeSort(start, end):
    global cnt
    if start < end:
        # 중간 값을 구한다
        mid = (start + end) // 2
        # 중간 값 기준으로 값을 쪼갠다(1개가 될 때까지)
        mergeSort(start, mid)
        mergeSort(mid+1, end)

        # a, b 리스트를 비교하며 담을 때 사용할 각 인덱스
        a = start
        b = mid + 1
        # print(a, b)
        # 정렬된 값을 담을 리스트
        tmp = []

        while a <= mid and b <= end:
            if arr[a] <= arr[b]:
                tmp.append(arr[a])
                a += 1
            else:
                # a 값이 더 클경우(원래 a값이 작아야하므로 swap이 발생)
                tmp.append(arr[b])
                b += 1
                # a(인덱스)에 따라 a 리스트끝(mid)에서 해당 인덱스 위치(a) 차(개수)만큼 더해줌
                cnt += (mid - a + 1)

        if a <= mid:
            tmp = tmp + arr[a:mid+1]
        if b <= end:
            tmp = tmp + arr[b:end+1]

        for i in range(len(tmp)):
            arr[start + i] = tmp[i]

        # print(arr)


if __name__ == '__main__':
    cnt = 0
    n = int(input())
    arr = list(map(int, input().split()))
    mergeSort(0, n-1)
    print(cnt)
