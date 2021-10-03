'''
goal : 원소가 반복문돌며 lst 안에 있는지 여부 확인 (1:있음/0:없음)
0. 라이브러리 입력 _ sys - 입력
1. 입력 받기
    1) 검색 대상 리스트 lst
    2) 검색할 리스트 search_list
3. search_list 돌며 요소 하나씩 이진탐색 호출 
4. 결과 출력
'''
# 0
import sys
imput = sys.stdin.readline


def is_there(target, start, end):
    if start > end:
        return False

    mid = (start+end)//2
    if obj_lst[mid] < target:
        return is_there(target, mid+1, end)
    elif obj_lst[mid] > target:
        return is_there(target, start, mid-1)
    else:
        return True
    # return False

    # 1
n = int(input())
obj_lst = sorted(list(map(int, input().split())))
m = int(input())
search_lst = list(map(int, input().split()))

start, end = 0, len(obj_lst)-1

# 2
for elem in search_lst:
    if is_there(elem, start, end):
        print(1)
    else:
        print(0)
