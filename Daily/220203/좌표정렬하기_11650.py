'''
>> P
2차원 평면 위 점 N개가 있을 때
x좌표 증가 순, 같으면 y좌표 증가 순으로 정렬 후 출력
    - 범위 : 값 / 개수 = ~ 10만
    - 같은 위치 점 없다

>> S
접근
입력을 받고 sorted() 사용하는데 key = lambda x, y = (x,y)
'''
import sys

input = sys.stdin.readline


N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

for x, y in sorted(arr, key=lambda x: (x[0], x[1])):
    print(x, y)

# print(*sorted(arr, key=lambda x: (x[0], x[1])), sep='\n')
