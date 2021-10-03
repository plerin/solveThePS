'''
goal : n개 랜선을 m개로 만들 때 최대 랜선 길이 구하라.
키워드 : n->m개 만드는데 최대 길이 + 범위가 커 == 이진탐색
0. 라이브러리 추가 _ sys : 입력 
1. 입력 받기
    1) K,N : 현재 랜선 수 / 필요 랜선 수 
    2) cables : 각 랜선 길이(cm) -> 정렬필요없어 _ 대상이 각 요소 값이 아닌 요소 - 중간 길이 뺀 값이라
2. 최소,최대 구하기 _ 0과 max(cables)
3. 최대 값 구하는 함수 호출 및 출력
'''
# 0
import sys

input = sys.stdin.readline


def getMaxLen(target, start, end):
    len = 0

    while start <= end:
        mid = (start+end)//2
        total = sum(map(lambda x: x//mid if x >= mid else 0, cables))

        if total < target:
            end = mid-1
        else:
            len = mid
            start = mid+1
    return len


# 1
k, n = list(map(int, input().split()))
cables = []
for _ in range(k):
    cables.append(int(input()))

# 2
start, end = 1, max(cables)

# 3
ret = getMaxLen(n, start, end)
print(ret)
