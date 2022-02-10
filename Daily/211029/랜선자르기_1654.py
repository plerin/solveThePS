'''
[P]
K개의 랜선을 갖고 있는데 N개의 길이가 같은 랜선을 만들어야 함 이 때 만들수 있는 최대 랜선 길이 구하라
    - K개를 N개로 만들어야 하는데 최대 길이 구하라
[S]
파라메트릭 서치 유형의 문제 == 이진탐색 == 최적화(예/아니요)문제를 이진 탐색을 하며 최적화 시킨다.
    - 유형 : 이진탐색 _ START/END/MID를 활용하여 적당한 길이를 구하라 _ 랜선을 만들 수 있을 때 저장하고 범위를 줄여가
[L]
1. 이진 탐색 준비물
    - START/END : 0, MAX(입력 랜선 리스트)
    - 이 유형에서는 정렬이 필요 없다
2. 입력 받기
    - K(int) : 갖고 있는 랜선 개수 / N(int) : 필요 랜선 개수
    - cables(list) : 랜선 리스트
3. 함수 선언
    - 목적 : n개 랜선을 만들 때 최대 랜선 길이 구하기
    - param : t(int) / s(int) / e(int)
    - logic :
        1) if s <= e then  -> get mid(s+e//2) -> cal total_num -> compare with t(target)
    - return
        : max_len(int)
4. 결과 출력
'''
import sys

input = sys.stdin.readline


def cutting_cable(t, s, e):
    max_len = 0
    while s <= e:
        mid = (s+e)//2
        total = sum(map(lambda x: x//mid if x >= mid else 0, cables))

        if total < t:
            e = mid-1
        else:
            max_len = mid
            s = mid+1

    return max_len


K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

start, end = 1, max(cables)

ret = cutting_cable(N, start, end)

print(ret)
