'''

youtube url -> https://www.youtube.com/watch?v=94RC-DsGMLo

>> Keyword
파라메트릭 서치
    -> 현재 이 높이로 자르면 조건 만족하는가' 만족 여부에 따라 탐색범위 좁혀 해결
범위가 0 ~ 10억
    -> 이렇게 큰 범위를 보면 '이진탐색'을 떠올려야함


>> P
절단기에 높이(h)를 지정하면 h보다 긴 떡은 윗 부분이 잘릴 것이거 낮은 떡은 잘리지 않음
손님이 요청한 길이가 m일 때 적어도 m만큼 떡을 얻기 위해 설정하는 절단기의 최댓값을 구하라
    - 범위 : N -> ~100만 // M -> ~ 20억

>> S
절단기 최대 높이 & 범위가 100만, 20억 -> 이진탐색으로 풀어보자

접근
1. 필요 조건인 정렬 수행
2. start, end, mid를 활용하여 절단기 높이가 mid일 때 떡을 얼마나 얻는지 확인
if val >= M then save mid(ret = mid) else 높이를 낮추기(end = mid - 1)
3. 결과 출력

코딩

import sys
input = 

N, M = input().split()
dduck = list(input().split())
dduck.sort()

print(get_height(dduck, 0, N-1))
def get_height(dduck, start, end) -> int:
    ret = 0

    while start <= end:
        mid = (start + end) // 2
        
        sumv = sum([height - mid for dduck if height >= mid])

        if sumv >= M:
            ret = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return ret
'''

import sys

input = sys.stdin.readline


def get_height(dduck: list, start: int, end: int) -> int:
    ret = 0

    while start <= end:
        mid = (start + end) // 2
        # 현재 높이로 떡의 양 계산
        sumv = sum([height - mid for height in dduck if height >= mid])
        # 떡의 양이 충분한 경우(왼쪽 탐색)
        if sumv >= M:
            ret = mid
            start = mid + 1
        else:
            end = mid - 1

    return ret


N, M = map(int, input().split())
dduck = list(map(int, input().split()))

dduck.sort()
# start = 0, end = 떡 중 가장 긴 값(max(dduck))
print(get_height(dduck, 0, max(dduck)))
