'''
goal : N에 여러 개 숫자가 있고 M에 여러 개 숫자가 있는데 M의 숫자가 N에 있는지 확인하라
0. 라이브러리 추가 _ SYS : 입력 
1. 입력 받기
    1) N(LIST) : 검색 대상 숫자들, M(LIST) : 검색 할 숫자들
2. N의 정렬 및 최소/최대 숫자 구하기
3. 이진탐색 함수 호출_재귀
    1) 종료조건(START > END) : NONE
    2) MID 찾고 TARGET과 비교하며 수행
4. 결과 출력
'''
import sys

input = sys.stdin.readline


def isThere(target, start, end):
    if start > end:
        return -1

    mid = (start+end)//2
    if n_lst[mid] < target:
        return isThere(target, mid+1, end)
    elif n_lst[mid] > target:
        return isThere(target, start, mid-1)
    else:
        return mid


# 1
n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

# 2
n_lst.sort()
start, end = 0, len(n_lst)-1
# 3
ret = []
for i in m_lst:
    if isThere(i, start, end) == -1:
        ret.append(0)
    else:
        ret.append(1)

# 4
print(*ret, sep='\n')
