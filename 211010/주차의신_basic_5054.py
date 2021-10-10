'''
goal : 주차를 하고 걸어야하는 거리의 최솟값 출력
1. 입력 받기
    1) T : 테스트 횟수
    2) N : 방문할 상점의 수
    3) stores : 상점의 위치
2. 로직
    1) 최소 거리 = (max-min)*2
'''
# 1
T = int(input())

for _ in range(T):
    n = int(input())
    stores = list(map(int, input().split()))
    print((max(stores)-min(stores))*2)
