'''
>> P
절단이 높이를 H로 지정하면 높이가 H보다 긴 떡은 나머지 만큼 잘린다.
요청한 길이가 M일 때 적어도 M만큼 떡을 얻기 위해 설정할 수 있는 옾이 최댓값을 구하라
    - 범위 : 떡의 개수는 100만 , 길이는 20억까지 
>> S
전형적인 파라메트릭 유형, 최적화(절단기 최대 높이)를 구하기 위해 yes/no 문제로 치환하여 풀이함
이진탐색으로 높이를 중간 길이를 구하고 해당 길이에서 구할 수 있는 떡이 목표치보다 많으면 높이고 적으면 낮추기
    - 높이가 mid일 때 얻을 수 있는 떡이 10이면 높이고(left = mid +1) 떡이 4이면 낮춘다(right = mid -1)
    -> 최초 길이 l = 0, right = 떡 길이 중 max 값  
'''


def solve(left: int, right: int) -> int:
    ret = 0

    while left <= right:
        mid = (left + right) // 2
        val = sum([h - mid for h in dduck if h > mid])

        if val < M:
            right = mid - 1
        else:
            ret = mid
            left = mid + 1

    return ret


N, M = map(int, input().split())
dduck = list(map(int, input().split()))

left, right = 0, max(*dduck)
ans = solve(left, right)

print(ans)
