'''
> P
2가지 연산을 수행한 결과를 출력하는 프로그램
    - R : REVERSE _ 뒤집기 // D : DELETE _ 버리기
    - 만약 배열에 값이 없는데 D가 나오면 "error"출력
> S
구현 _ 
1. [1,2,3,4]를 리스트 형태로 입력 받기 _ arr = list(map(int, input()[1:-1].split(",")))
2. R : [::-1] D : popleft() _ deque 이용
'''
from collections import deque
import sys

# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     func = deque(list(map(str, input())))
#     n = int(input())
#     arr = input()[1:-1]
#     if len(arr) == 0:
#         queue = []
#     else:
#         queue = deque(list(map(int, arr.split(","))))

#     while func:
#         f = func.popleft()
#         if f == 'R':
#             queue.reverse()
#         else:
#             if len(queue) != 0:
#                 queue.popleft()
#             else:
#                 queue = None
#                 break

#     if queue == None:
#         print('error')
#     else:
#         print(f'[{",".join(map(str,queue))}]')


T = int(input())

for _ in range(T):
    func = deque(list(map(str, input())))
    n = int(input())
    arr = input()[1:-1]
    if len(arr) == 0:
        queue = []
    else:
        queue = deque(list(map(int, arr.split(","))))

    start, end = 0, len(queue)-1

    while func:
        f = func.popleft()
        if f == 'R':
            arr = arr[::-1][:(end-start)]
        else:
            if start < end:
                start += 2
            else:
                break

    if len(arr) == 0:
        print('error')
    else:
        print(f'[{arr}]')
