'''
goal : 스티커 중 가장 높은 점수 리턴 (인접_상하좌우는 못함)
1. 입력 받기
    1) T(int): 테스트 횟수
    2) N(int) : 2행 n열을 의미
    3) n열 요소(list) 
    => s 이중배열에 담기
2. 동적계획법 수행
3. 결과 반환
'''

T = int(input())
for i in range(T):
    n = int(input())
    s=[list(map(int,input().split())) for _ in range(2)]

    d = [[0] * 100000 for _ in range(2)]
    ret = []

    # d[0][0] = max(s[0][0],s[1][0])
    # d[1][0] = max(s[0][0],s[1][0])
    # d[0][1] = max(s[0][0],s[1][0]+s[0][1])
    # d[1][1] = max(s[1][0],s[0][0]+s[1][1])

    # 여기서 d[0][5]는 0번째 행렬에서 5를 체크하는 가장 큰 점수를 의미
    for i in range(n):
        if i == 0:
            d[0][i] = s[0][0]
            d[1][i] = s[1][0]
        elif i == 1:
            d[0][i] = s[1][0]+s[0][1] # 여기서 d[0][1]이면 0번째 행에서 1번째 열을 선택하는 가장 큰 점수를 의미
            d[1][i] = s[0][0]+s[1][1]
        else:
            d[0][i] = s[0][i] + max(d[1][i-2],d[1][i-1])
            d[1][i] = s[1][i] + max(d[0][i-2],d[0][i-1])
            # d[0][i] = max(d[0][i-1],d[1][i-1]+s[0][i],d[0][i-2]+s[0][i],d[1][i-2]+s[0][i])
            # d[1][i] = max(d[1][i-1],d[0][i-1]+s[1][i],d[1][i-2]+s[1][i],d[0][i-2]+s[1][i])
        
        # ret.append(max(d[0][i],d[1][i]))

    print(max(d[0][n-1],d[1][n-1]))

# T = int(input())
# for i in range(T):
#     n = int(input())
#     s=[list(map(int,input().split())) for _ in range(2)]

#     d = [0] * 100000

#     d[0] = max(s[0][0],s[1][0])
#     d[1] = max(s[1][0]+s[0][1],s[0][0]+s[1][1])

#     for i in range(2,n):
#         d[i] = max(d[i],d[i-1]+s[0][i],d[i-2]+s[0][i] , d[i],d[i-1]+s[1][i],d[i-2]+s[1][i])
    
#     print(d[n-1])
