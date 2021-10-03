'''
0. 라이브러리 추가 _ sys - 입력 
1. 입력 받기
    1) n,m : 떡 개수, target(목표 길이)
    2) rice_cakes : 한 줄로 구현
2. 함수 호출
    1) 인자 : target, start, end
    2) target보다 크고 작은 경우 재귀 호출 _ ==target이 아닌경우 없다고 가정
3. 결과 출력 
'''
import sys

input = sys.stdin.readline


def getMaxHeight(target, start, end):
    if start > end:
        return None

    mid = (start+end)//2
    sum_v = sum(map(lambda x: x-mid if x > mid else 0, lst))

    if sum_v > target:
        # ret = mid
        return getMaxHeight(target, mid+1, end)
    elif sum_v < target:
        return getMaxHeight(target, start, mid-1)
    else:
        return mid

# 반복문


def getMaxHeight(target, start, end):
    ret = 0  # 자른 떡이 요구 떡보다 클 경우 계속 갱신

    while start <= end:
        mid = (start+end) // 2
        total = sum(map(lambda x: x-mid if x > mid else 0, lst))

        if total < target:  # 만약 자른 떡이 요구 값보다 부족할 때 end -1
            end = mid - 1

        else:
            ret = mid  # 만약 자른 떡이 요구 값보다 큰 경우 start+1 그리고 ret 갱신
            start = mid + 1
    return ret


# 1
n, target = list(map(int, input().split()))
lst = list(map(int, input().split()))

# 시작과 끝을 설정
start, end = 0, max(lst)

ans = getMaxHeight(target, start, end)
print(ans)
