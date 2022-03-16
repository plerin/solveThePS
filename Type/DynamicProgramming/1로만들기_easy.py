'''
youtube url -> https://www.youtube.com/watch?v=5Lu34WIx2Us&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=6&t=22s

>> Keyword

>> P
정수 X가 주어졌을 때 사용할 수 있는 연산이 4가지
1. 5로 나누어 떨어지면 5로 나누기
2. 3으로 나누어 떨어지면 3으로 나누기
3. 2로 나누어떨어지면 2로 나누기
4. 1을 빼기
연산 사용 최솟값을 구하라

>> S

접근
1. 어떤 유형인지 파악 
떠오르는건 완전탐색, 그리디, 동적할당
최고 효율을 선택하는 그리디는 이문제에서 적합하지 않아-> 1을 빼는게 효율적인 경우가 있으니

2. 점화식을 세워보자
d(n) = 정수 n을 1로만드는데 필요한 최소 연산 횟수
d(n) = min(d(n/5), d(n/3), d(n/2), d(n-1)) + 1 단, n%5/3/2 == 0인 경우에만 나누기
-> 동적계획법 필요조건 2가지 충족

코딩
1. 입력 받기 
x = int(input())
2. 로직 필요 변수 선언
dp = [0] * (x+1)
3. 함수 호출
print(solve(x))
4. 함수 생성
def solve(num: int) -> int:
    global dp

    dp[1] = 1

    for i in range(2, x+1):
        if i % 5 == 0:
            dp[i] = dp[i//5] + 1
        elif i % 3 == 0:
            dp[i] = dp[i//3] + 1
        elif i % 2 == 0:
            dp[i] = dp[i//2] + 1
        else:
            dp[i] = dp[i-1] + 1
    
    return dp[num]

'''
INF = float('inf')


def solve(num: int) -> int:
    global dp

    dp[1] = 0

    for i in range(2, x+1):
        if i % 5 == 0:
            dp[i] = dp[i//5]
        elif i % 3 == 0:
            dp[i] = dp[i//3]
        elif i % 2 == 0:
            dp[i] = dp[i//2]

        dp[i] = min(dp[i-1], dp[i]) + 1

    return dp[num]


x = int(input())
dp = [INF] * (x+1)

print(solve(x))
