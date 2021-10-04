'''
goal : 식량창고를 최대한 많이 약탈하는 경우 구하기(인접창고 불가)
문제 풀이 방법
1. 경우의 수를 구해 최적해 구해보기
2. 최적해 구하는 방법을 통해 점화식 구하기
3. 점화식을 코드로 구현
'''

n = int(input())
array = list(map(int, input().split()))

# dp 테이블 초기화
d = [0] * 100

# 바텀업 로직 진행
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

# 계산 결과 출력
print(d[n-1])
