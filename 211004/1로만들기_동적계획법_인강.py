'''
goal : 숫자 x를 1로 만들기 위해 최소 횟수 반환 _ 아래 연산만 수행 가능
    1. 5로 나누어 떨어지면 5로 나누기
    2. 3로 나누어 떨어지면 3로 나누기
    3. 2로 나누어 떨어지면 2로 나누기
    4. 1빼기
풀이 방법
1. 최적해 구하는 방식으로 바꿔보기
    1) ai = i를 1로 만드는 최소 횟수라고 한다면
    2) ai => ai-1, ai/2, ai/3, ai/5 중 가장 작은 값을 선택하고 하는 최적 구분 구조 성립
    3) a3,a5 등은 더 큰 값을 구할 때 중복되서 사용되므로 중복 구분 구조 성립
    4) 점화식 : ai = min(ai-1,ai/2,ai/3,ai/5)+1 , 여기서 2,3,5는 나누어 지는 경우만 고려 
'''

# 입력 받기
x = int(input())

# 앞선 결과 저장위한 dp 테이블 초기화
d = [0] * 30001  # 1~30000 노드

# 다이나믹 프로그래밍 바텀업
for i in range(2, x+1):
    d[i] = d[i-1]+1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])
