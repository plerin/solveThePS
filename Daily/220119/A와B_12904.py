'''
>> P
A와 B로 이루어진 영어 단어가 있고 문자열 S와 T가 주어졋을 때
2가지 연산을 통해서 S를 T로 만들 수 있는지 여부 출력
    - 연산
        1) 문자열 뒤에 A를 추가
        2) 문자열 뒤집고 B를 추가
>> S    
S에서 T를 만드는 경우보다 T에서 S를 만드는 경우가 더 간단해
연산을 반대로 생각해보자(T -> S)    
    - 문자열 뒤에 A가 있으면 A제거
    - 문자열 뒤에 B가 있으면 B제거 후 뒤집기

>> C
1. dfs 활용
def dfs(t: str) -> int:
    # 반환값 초기화(0)
    ret = 0 
    # 기저 조건 _ 길이가 같다면
    if len(t) == len(S):
        if t == S:
            ret = 1
        return
    
    # 2가지 경우(맨 뒤가 'A'인 경우 / 맨 뒤가 'B'인 경우) 처리 후 재귀 호출
    if t[-1] == 'A':
        t.pop()
        ret = dfs(t)
        t.append('A')
    
    if t[-1] == 'B':
        t.pop()
        t = t[::-1] # 뒤집기
        ret = dfs(t)
        t = t[::-1]
        t.append('B')
    
    return ret

2. 반복문 활용

def posible_convert(t: str) -> int:
    
    while len(t) != len(S):
        if t[-1] == 'A':
            t.pop()
        elif t[-1] == 'B':
            t.pop()
            t = t[::-1]
    
    return 1 if t == S else 0

'''
import sys
sys.setrecursionlimit(10**7)

def dfs(t: str) -> int:
    # 반환값 초기화(0)
    ret = 0
    # 기저 조건 _ 길이가 같다면
    if len(t) == len(S):
        if t == S:
            ret = 1
        return ret

    # 2가지 경우(맨 뒤가 'A'인 경우 / 맨 뒤가 'B'인 경우) 처리 후 재귀 호출
    if t[-1] == 'A':
        t.pop()
        ret = dfs(t)
        t.append('A')

    if t[-1] == 'B':
        t.pop()
        t = t[::-1]  # 뒤집기
        ret = dfs(t)
        t = t[::-1]
        t.append('B')

    return ret


def posible_convert(t: str) -> int:

    while len(t) != len(S):
        if t[-1] == 'A':
            t.pop()
        elif t[-1] == 'B':
            t.pop()
            t = t[::-1]

    return 1 if t == S else 0


S, T = [list(input()) for _ in range(2)]

# print(dfs(T))
print(posible_convert(T))
