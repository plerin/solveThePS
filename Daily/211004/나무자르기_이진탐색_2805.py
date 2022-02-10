'''
goal : N개의 나무에서 M의 나무가 필요할 때 절단기 높이 최댓 값 구하기
0. 라이브러리 추가 _ SYS:입력
1. 입력 받기
    1) N,M : (나무 수/필요 나무 길이)
    2) trees : 나무 각 높이 리스트
2. 최소/최대 값 구하기
    1) trees를 활용
3. getMaxHeight() 호출
4. 결과 출력
'''
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
            max_v = max(max_v, mid)
            start = mid+1
    return max_v


# 0
n, m = list(map(int, input().split()))
trees = list(map(int, input().split()))

# 2
start, end = 1, max(trees)

# 3
ret = getMaxHeight(m, start, end)

# 4
print(ret)
