'''
goal : 나무 m개(높이가 일정치 않은) 중 일정 높이만큼 자르고 남은 나무 필요(m) 이 때 최댓 값 구하라
0. 라이브러리 추가 _ sys : 입력
1. 입력 받기
    1) N,M : 나무 수 / 필요한 나무 길이(TARGET)
    2) TREES : 각 나무 높이
3. 최소 최대 값 구하기  _ 1(1이상), MAX(TREES)
4. 최대 길이 구하는 함수 호출 및 결과 리턴
'''
# 0
import sys

input = sys.stdin.readline


def getMaxHeight(target, start, end):
    max_v = 0

    while start <= end:
        mid = (start+end)//2
        total = sum(map(lambda x: x-mid if x > mid else 0, trees))

        if total < target:
            end = mid-1
        else:
            max_v = mid
            start = mid+1

    return max_v


# 1
n, m = list(map(int, input().split()))
trees = list(map(int, input().split()))

# 2
start, end = 1, max(trees)

ret = getMaxHeight(m, start, end)
print(ret)
