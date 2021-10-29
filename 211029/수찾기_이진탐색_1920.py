'''
[P]
N개의 정수가 주어졌을 때 정수(X)가 존재하는지 알아내는 프로그램
    - N / X 범위 모두 1~10만, 값의 범위는 INT범위
[S]
단순히 탐색 문제인데 범위가 너무 커서 선형탐색으로 시간초과 나오겠다.
    - 유형 : 이진탐색 _ 정렬해서 이진탐색으로 X 존재 여부 확인
[L]
1. 입력 받기
    - N(int) : 개수 , n_arr(list) : 리스트
    - M(int) : x 개수, m_arr(list) : x 리스트
2. 이진 탐색 필요 조건
    - 검색 대상인 n_arr 정렬(오름차순)
    - start/end/mid 사용함에 있어서 start/end 지정 
3. 함수 선언
    - 목적 : 해당 값이 n_arr에 존재하는지 여부 파악
    - param : x(int) / start(int) / end(int)
    - logic : start<=end 인경우 mid 찾아가기
    - return : -1/index
4. 결과 출력
'''


def find(target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if n_arr[mid] == target:
            return mid
        elif n_arr[mid] < target:
            start = mid+1
        else:
            end = mid-1

    return -1


N = int(input())
n_arr = list(map(int, input().split()))
M = int(input())
m_arr = list(map(int, input().split()))

start, end = 0, len(n_arr)-1
n_arr.sort()

for e in m_arr:
    exist = find(e, start, end)

    if exist == -1:
        print(0)
    else:
        print(1)
