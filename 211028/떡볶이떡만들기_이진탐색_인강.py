'''
[P]
전단기 높이(H)를 사용하여 적어도 M만큼 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 쵀댓값을 구하라
    - 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고 낮은 떡은 잘리지 않는다
[S]
최적화된 높이를 찾는 문제는 파라메트릭 서치 유형이고 이진탐색으로 풀이 & 값의 범위가 엄청 크다
    - 유형 : 이진탐색 _ 높이의 최댓 값
[L]
0. 이진탐색 풀이법
    - START / END / MID 를 사용하여 범위를 절반씩 줄여나간다 -> O(logN)
1. 입력 받기
    - N(int) : 떡의 개수 / M(int) : 떡의 길이
    - dduck(list) : 떡의 길이
2. 함수 호출
    - 목적 : 이진탐색하며 m만큼의 떡을 자르며 설정할 수 있는 높이 최댓값
    - PARAM : target(int) / start(int) / end(int)
    - LOGIC
        1) MID 값을 구하고 해당 길이에서 TARGET과 비교한다
        2) 
'''

n, m = map(int, input().split())
dduck = list(map(int, input().split()))

ret = 0
start, end = 0, max(dduck)

while start <= end:
    mid = (start+end) // 2
    total = 0
    for x in dduck:
        if x > m:
            total += x-mid

    if total < m:
        end = mid - 1
    else:
        ret = mid
        start = mid + 1

print(ret)
