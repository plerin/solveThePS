'''
goal : N개의 정수 중 v 개수 반환
1. 입력 받기
    1) N : 정수 개수
    2) lst : 정수 리스트
    3) V : 찾는 정수
2. map(lambda)의 len반환
'''

N = int(input())
lst = list(map(int, input().split()))
V = int(input())
# print(len(list(filter(lambda x: x == V, lst))))
print(lst.count(V))
