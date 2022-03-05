'''
youtube url -> https://www.youtube.com/watch?v=5Lu34WIx2Us&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=6&t=22s

>> Keyword

>> P
식량창고가 리스트 형태로 주어질 때 얻을 수 있는 식량의 최댓값을 구하라
    - 최소 한 칸 이상 떨어진 식량창고 약탈해야함

>> S
접근
1. 문제의 유형(알고리즘)을 알아낸다.
완전탐색 or 동적계획
2. 동적계획 필요조건(최적부분,중복부분) 만족하는지?
- 점화식 : d(n) = max(d(n-2) + k, d(n-1)), k = 현재 식량값, d(1)&d(2)는 구할 수 있음
두 가지 필요조건 만족 -> 상향식방법풀기

코딩
1. 입력 받기
n과 store
2. 연산 필요 변수 선언
MAX = 101(100까지니까)
dp = [0] * MAX
3. 함수 호출
print(max_food(n))
4. 함수 선언
def max_food(num: int) -> int:
    global dp
    
    dp[0] = store[0]
    dp[1] = max(dp[0], store[1])

    for i in range(2, MAX):
        dp[i] = max(dp[i-2] + store[i], dp[i-1])
    
    return dp[num]
'''


def get_food2(num: int) -> int:
    if num < 2:
        return max(store[:num+1])

    if dp[num] != 0:
        return dp[num]

    dp[num] = max(get_food2(num-2) + store[num], get_food2(num-1))
    return dp[num]


def get_food(num: int) -> int:
    global dp

    dp[0] = store[0]
    dp[1] = max(store[0], store[1])

    for i in range(2, n):
        dp[i] = max(dp[i-2] + store[i], dp[i-1])

    return dp[num-1]


n = int(input())
store = list(map(int, input().split()))

dp = [0] * n

print(get_food2(n-1))
