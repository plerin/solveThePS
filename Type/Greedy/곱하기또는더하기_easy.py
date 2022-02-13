'''
youtube url -> https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2&t=758s

>> Keyword
그리디 알고리즘, 아이디어를 발견하고 정당성으로 검증

>> P
0부터 9로만 이루어진 문자열 S가 주어졌을 때
'*', '+' 연산을 넣어 만들 수 있는 가장 큰 수를 구하라
    - 모든 연산은 왼쪽부터 순서대로 실행

>> S
가장 큰 수를 구하려면 언제 '+'를 사용할지 알면 돼
- [0, 1]인 경우는 곱하는 것보다 더하는게 효율적
- 2~9까지는 곱하는게 효율적
    -> 0 ~ n-1을 탐색하며 i와 i+1번째 값 중 0,1이 있는지 확인하고 있으면 + 없으면 *

정당성검증
1. '+' 보다 '*' 가 값을 더 크게 해줌
    단, 0과 1인 경우 제외

코드
ret = [0]
for i in range(1,len(S)):
    if ret , [i] in (0, 1):
        ret += 
    else:
        ret *= [i]

'''


def solve(arr: list) -> int:
    ret = arr[0]

    for i in range(1, len(arr)):
        if ret in (0, 1) or arr[i] in (0, 1):
            # if ret <= 1 or arr[i] <= 1
            ret += arr[i]
        else:
            ret *= arr[i]

    return ret


S = list(map(int, input()))

print(solve(S))
