'''
1. 테스트 횟수 입력 받아 반복
2. 자연수 개수(n)은 의미 없지만 받아
3. 입력수를 map(sum)으로 출력 
'''

for _ in range(int(input())):
    n = int(input())
    print(sum(map(int, input().split())))
