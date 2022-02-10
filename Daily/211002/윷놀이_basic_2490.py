'''
goal : 윷놀이 던저 나온 결과를 A-E로 출력
1. 입력 받기_ 3번 
2. DABCD 리스트 만들고 SUM에 따라 매칭 출력
'''
lst = 'DCBAE'
ret = [lst[sum(map(int, input().split()))] for _ in range(3)]
print(*ret, sep='\n')
