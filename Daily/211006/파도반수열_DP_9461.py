'''
GOAL : 파도반 수열에서 규칙을 찾아 점화식을 만들고 P(N)을 구하라
0. 라이브러리 추가 _ 없음
1. 입력 받기
    1) T = 테스트 경우
    2) T라인 동안 N 입력 받아 결과 반환
2. DP 로직
    1) 사전 조건(최적 구조, 중복 구조 확인)
    2) 최적해 구해보기
    3) 점화식 작성
    4) 코드로 구현 및 IGNITE
'''

#0

#1
T = int(input())

for i in range(T):
    n = int(input())
    d = [0] * n

    # d[0]=d[1]=d[2]=1

    for i in range(n):
        if i < 3:
            d[i] = 1
        else:
            d[i] = d[i-3]+d[i-2]
    
    print(d[n-1])