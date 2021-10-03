'''
goal : 오름차순 정렬된 수열에서 원소 x의 개수를 구하기 + logN 시간복잡도 
0. 라이브러리 사용 _ bisect - left/right를 통해 lst에서 해당 문자의 가장 왼쪽/오른쪽 인덱스 구하기
1. 입력 받기
    1) n,x -> 배열 원소 개수, 찾고자하는 원소
    2) 수열 -> lst에 담기
2. bisect를 활용해 해당 lst에서 가장 왼쪽/오른쪽 인덱스 구해서 개수 반환 함수 작성
3. 함수 호출 값 반환
'''
# 0
from bisect import bisect_left, bisect_right


def count_by_value(lst, target):
    left_idx = bisect_left(lst, target)
    right_idx = bisect_right(lst, target)
    return right_idx-left_idx


# 1
n, x = list(map(int, input().split()))
num_lst = list(map(int, input().split()))

# 2
ret = count_by_value(num_lst, x)
# 3
print(ret)
