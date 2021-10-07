'''
goal : 양의 정수 n을 이진수로 변환했을 때 1의 위치를 나열
0. 라이브러리 추가 : 없음
1. 입력 받기
    1) T = 테스트 횟수
    2) N = 이진수로 바꿀 정수
2. 로직
    1) 테스트 횟수 만큼 반복
    2) RET(LIST) 초기화 하고 bin(n)[::-1] 돌며 isdigit() and '1'이면 ret에 추가
    3) 출력
'''

#1
for _ in range(int(input())):
    ret = []
    n = bin(int(input()))[::-1]
    for i,v in enumerate(n):
        if v == '1':
            ret.append(i)
    print(*ret)
    