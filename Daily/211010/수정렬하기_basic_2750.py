'''
goal : N개를 입력받아 오름차순 절열한 결과를 한 줄에 하나씩 출력
1. 입력 받기
    1) N : 정수 개수
    2) lst : 정수 구성 값
2. 로직
    1) sorted()한 리스트를 sep='\n'로 출력
'''
# 1
N = int(input())
lst = [int(input()) for _ in range(N)]

print(*sorted(lst), sep='\n')
