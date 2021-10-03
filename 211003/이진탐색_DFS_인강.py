'''
이진 탐색 DFS로 구현
1. 입력 받기 
2. 이진 탐색 함수(DFS) 호출
    1) 종료조건 작성
    2) 로직
3. 결과 출력
'''


def binary_search(target, start, end):
    if start > end:
        return None

    mid = (start+end) // 2
    if array[mid] < target:
        start = mid+1
        return binary_search(target, start, end)
    elif array[mid] > target:
        end = mid-1
        return binary_search(target, start, end)
    else:
        return mid

# def binary_search(target, start, end):
#     while start <= end:
#         mid = (start+end)//2

#         if array[mid] < target:
#             start = mid+1
#         elif array[mid] > target:
#             end = mid-1
#         else:
#             return mid

#     return None


# 1
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# 2
ret = binary_search(target, 0, n-1)  # 리스트,타겟,start,end

if ret == None:
    print('원소가 존재하지 않아')
else:
    print(ret+1)
