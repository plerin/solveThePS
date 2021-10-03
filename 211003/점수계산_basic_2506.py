'''
goal : 문제 점수 계산 _ 연속으로 맞추면 가산점 부여
0. 라이브러리 추가 _ sys : 입력 / deque : 큐 사용 
1. 입력 받기 
    1) 점수 리스트는 deque에 담아
2. deque에서 하나씩 빼며 0/1 구분하여 로직 수행
'''
from collections import deque
import sys

input = sys.stdin.readline

# 1
n = int(input())
score_lst = deque(list(map(int, input().split())))
# score_lst.append(0)
# cnt, ret = 0, 0
# while score_lst:
#     elem = score_lst.popleft()
#     if elem == 0:
#         ret += (cnt*(cnt+1))//2
#         cnt = 0
#     else:
#         cnt += 1

# print(ret)

r = c = 0
for i in score_lst:
    if i == 0:
        c = 0
    else:
        c += 1
    r += c

print(r)
