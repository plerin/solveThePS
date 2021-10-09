'''
goal : n개의 화폐를 이용해 m원을 만드는데 최소 개수 구하라
1. 입력 받기
    1) N,M : 화폐 종류, 목표 금액
로직
    1) dp 테이블 초기화 : m+1 만큼 무한으로(inf)
    2) 다이나믹 프로그래밍 
        1) d[0] 초기화
        2) 동전종류와 최대값(m+1)으로 반복문 돌기
    3) 결과 출력
'''

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

# # 로직
# d = [10001] * (m+1)  # 여기서 무한(10001)를 최댓값(m+1)만큼 초기화

# d[0] = 0  # 0만드는데 필요한 개수
# for i in range(n):
#     for j in range(array[i], m+1):  # 최대 값까지 갱신
#         if d[j-array[i]] != 10001:  # (i-k)원을 만드는 방법이 존재하는 경우
#             d[j] = min(d[j], d[j-array[i]] + 1)  # 기존 d[j] 개수와 다른 화폐이용했을 경우를 비교
# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
