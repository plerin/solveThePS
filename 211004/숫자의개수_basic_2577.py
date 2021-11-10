'''
goal : 세 자연수(a,b,c)의 합에서 0~9까지 개수를 출력
1. 입력 받기
    1) 세 수를 입력 받아 곱을 만들어
2. 로직 수행
    1) map(int,str()) 으로 각 자리 수가 독립된 리스트 만들기
    2) for i in range(10) 돌면서 == i 인 수를 리스트로 만들기
3. 결과 출력
'''
# 1
multiple = 1
for _ in range(3):
    multiple *= int(input())

# 2
multiple = list(map(int, str(multiple)))
ret = [len(list(filter(lambda x: x == i, multiple))) for i in range(10)]

# 3
print(*ret, sep='\n')
