'''
goal : 두 수를 입력 받아 거꾸로 읽은 수 중 큰 수를 반환
1. 입력 받기
    1) 거꾸로 입력 받고 int로 변환 후 max 값 출력
'''

print(max(map(int, map(lambda x: x[::-1], input().split()))))
