'''
goal: 8개 점수 중 높은 5개 점수의 총 합과 해당 문제 번호를 ' '로 구분하여 반환
0. 라이브러리 추가 _ import heapq : 점수 높은 순대로 5개 뽑기 위함
1. 입력 받기
    1) 8줄에 걸쳐 점수를 입력 받는다 -> heapq에 (-score,idx)
2. 로직
    1) 5번 반복하며(heapq) 점수는 더하고 인덱스는 모은다 -> sum_v, idx
    2) 결과 출력 
'''
import heapq

# 1
q = []
for i in range(1, 9):
    heapq.heappush(q, (-int(input()), i))

sum_score, idx = 0, []

for _ in range(5):
    score, i = heapq.heappop(q)
    sum_score += score*-1
    idx.append(i)

print(sum_score)
print(*sorted(idx), sep=' ')
