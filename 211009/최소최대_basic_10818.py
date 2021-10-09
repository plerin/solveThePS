'''
goal : N개의 정수에서 최소/최대 값 반환
'''

N = int(input())
lst = list(map(int, input().split()))
print(min(lst), max(lst))
