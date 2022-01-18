'''
>> P
a와 b로 이루어진 단어가 있다.
문자열 s와 t가 주어졌을 때 s를 t로 바꿀 수 있는지 여부 확인하라
    - 문자열 뒤에 a를 추가한다
    - 문자엘 뒤에 b를 추가하고 문자열을 뒤집는다.
>> S
작은 a와 큰 b가 있을 때
큰 b를 작은 a로 만들면 문제가 간단해짐

a -> b : 문자열 뒤에 a를 추가한다 
b -> a : 문자열 뒤에 a를 제거한다
---
a -> b : 문자열 뒤에 b를 추가하고 뒤집는다.
b -> a : 문자열을 뒤집고 뒤에 b를 제거한다
b가 a길이가 될 때까지 수행 뒤 같은 지 확인하고 아니라면 불가능한 것
>> C
S = list(input())
T = list(input())

while len(T) != len(S):
    if T[-1] == 'A':
        T.pop()
    else:
        T.reverse()
        if T[-1] != 'B':
            break
        T.pop()

if T == S:
    print(1)
else:
    print(0)


뒤집고 b를 빼는 연산도 a를 빼는 연산도 모두 줄어드는 연산이니까 끝이 있어
모든 후보를 []에 담아놓고 하나씩 2연산 모두 수행 후 []에 다시 담아줘 
    그 과정속에 T가 있으면 return 없으면 print(0)
'''
# from collections import deque

# S = list(input())
# T = list(input())

# candidate = deque([T])  # deque에 T으로 초기화

# ans = 0

# while candidate:
#     str = candidate.popleft()

#     if str == S:    # 연산 중 S를 만나면 성공
#         ans = 1
#         break

#     if str and str[-1] == 'A':  # 문자열 마지막 값이 'A'라면
#         candidate.append(str[:-1])

#     if str and str[::-1][-1] == 'B':    # 문자열 뒤집고 마지막 값이 'B'라면
#         candidate.append(str[::-1][:-1])

# print(ans)


'''
dfs 풀이 
조건에 따라 경우가 2가지로 나뉜다.
1. [-1] == 'A' 인경우
2. [0] == 'B' 인 경우 
두 경우에 따라 처리하는 것이 다르다 pop() or reverse() & pop()
그리고 기저조건이 있다. 줄어든 T의 길이가 S와 같은지 그리고 값까지 같으면 print(1) exit()

'''


def dfs(val: str) -> None:
    if len(val) == len(s):
        if val == s:
            print(1)
            exit(0)
        return

    if val[0] == 'B':
        val = val[::-1]
        val.pop()
        dfs(val)
        # val[0] == 'B' 연산이 아래 줄에 있는 val[-1] == 'A'연산에 영향을 주기 때문에 다시 초기화 해야함
        val.append('B')
        val = val[::-1]

    if val[-1] == 'A':
        val.pop()
        dfs(val)
        # 위 이유와 마찬가지로 다시 초기화
        val.append('A')


if __name__ == '__main__':
    s, t = [list(input()) for _ in range(2)]
    dfs(t)
    print(0)
