'''
goal : 오타를 지운 문자열 출력
1. 입력 받기
    1) n : 테스트 횟수
    2) 위치 문자 : 문자는 인덱스 1부터 시작
키워드 : 슬라이싱
'''

T = int(input())
ret = []
for _ in range(T):
    print(list(map(lambda x: x, input().split())))
    # list(map(lambda x: x[1][:int(x[0])-1]+x[1][int(x[0]):], input().split())))

# print(*ret, sep='\n')
