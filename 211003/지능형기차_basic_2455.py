'''
goal : 4 정차역을 지나며 타고내리는데 가장 많은 사람이 타고 있는 경우를 출력
0. 라이브러리 추가 _ sys : 입력
1. 입력 받기
    1) 각 정차역마다 out / in  -> max,cur 값 두고 진행
2. 결과 리턴
'''
import sys

input = sys.stdin.readline

# 1
ret = cur = 0
for _ in range(4):
    off, on = list(map(int, input().split()))
    cur = cur + (on-off)
    ret = max(ret, cur)

print(ret)
