'''
goal : 5명의 총점을 계산하고 우승자 번호와 점수출력
0. 라이브러리 추가 _ heapq : (-점수,번호)
1. 입력 받기
    1) 5번 반복하며 점수받기 _ 번호가 필요해서 range(1,6)으로 진행
    2) sum을 heapq에 담아 : (-점수,번호) 형태
2. 결과 출력
    1) heappop으로 1개 뽑아 출력
'''
#0
import heapq

#1
ret = []
for i in range(1,6):
    sum_v = sum(map(int,input().split()))
    heapq.heappush(ret,(-sum_v,i))

#2
score, i = heapq.heappop(ret)
print(i,score*-1)