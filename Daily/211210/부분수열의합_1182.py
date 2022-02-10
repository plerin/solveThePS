'''
> P
N개 정수로 이루어진 수열 부분수열 중 원소의 합이 S인 경우의 수를 구하라

> S
1. 정수의 개수가 1~20이니까 이걸 비트마스크로 저장 
    - 부분수열에 1,3,5 순서 값이 사용됐으면 1<<3 , 1<<5, 1<<1 인 상태로 저장
    - 부분수열 구할 때 반복문들 돌릴텐데 (part >> i) & 1 으로 값 사용여부 확인
        -> 재귀로 돌며 bc : if part == (1 << N) -1 then return

function
    - param : depth(int) _ 부분수열 개수
    - vari : S(int) _ 원하는 합, ret(int) _ 결과 값, part(int) _ 부분수열 값(비트마스크)
    - logic :
        1) part sum 값 확인 if sum == S then return
        2) 아니다 어짜피 part에 꽉차면 안하니까 재귀 return을 걸어놓자
        3) for i in range(N) -> if (part >> i) & 1 then continue -> solve(depth+1)
    - return 
'''


def solve(depth: int, part: list):
    global ans

    if


N, S = map(int, input().split())
seq = list(map(int, input().split()))
ans = 0

solve(0, [])

print(ans)
