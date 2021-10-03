'''
0. 라이브러리 추가 _ sys : 입력 
1. 입력 받기
    1) n : 개수 
    2) scores : 각 과목 점수 _ list
2. 가장 큰 값 찾기 _ max(scores)
3. 값 변환 및 결과 반환
    1) n/max *100 의 sum avg 
'''
# 0
import sys

input = sys.stdin.readline

# 1
n = int(input())
scores = list(map(int, input().split()))

# 2
max_v = max(scores)

# 3
print(sum(map(lambda x: (x/max_v)*100, scores))/len(scores))
