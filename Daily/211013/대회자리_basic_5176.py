'''
goal : 참가자(P)와 자리(M)이 주어질 때 대회에 참가하지 못하는 사람 수(자리에 못 앉는 수)를 구하라
0. 라이브러리 추가 
1. 입력 받기
    1) K : 테스트 횟수 _ LOOP
    2) P,M : 참가자 수, 자리 수
    3) 참가자가 원하는 자리 
2. 로직
    1) M만큼 0인 리스트 만들어
    2) 원하는 자리에 해당하는 자리를 0->1로 갱신
    3) 요소 값이 1인 리스트 길이 구해서 반환
'''

# 1
K = int(input())
for _ in range(K):
    p, m = map(int, input().split())
    seats = [0 for _ in range(m)]
    for i in range(p):
        seats[int(input())-1] = 1

    print(p-len(list(filter(lambda x: x == 0, seats))))
