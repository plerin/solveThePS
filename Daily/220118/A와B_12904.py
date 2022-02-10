'''
>> P
A와 B로만 영어단어가 존재
문자열 S와 T가 주어졌을 때 S를 T로 만들 수 있는지 여부 확인
    - 문자열 뒤에 A를 추가
    - 문자열 뒤집고 뒤에 B를 추가
>> S
s에서 t를 만들어야 한다 == t를 s로 만들어야 한다
작은 값 S에서 큰 값인 T를 만들어야 한다는 것은
똑같은 규칙을 반대로 적용해서 큰 값인 T에서 작은 값 S를 만들 수 있는가 여부를 확인해보면 된다.

S = list(input())
T = list(input())

while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()

if T == S:
    print(1)
else:
    print(0)


'''


# S = list(input())
# T = list(input())

# while len(S) != len(T):
#     if T[-1] == 'A':
#         T.pop()
#     elif T[-1] == 'B':
#         T.pop()
#         T.reverse()

# if T == S:
#     print(1)
# else:
#     print(0)

# dfs로 풀어보기

'''
>> 접근
문자열 S와 T가 주어졌을 때 S를 T로 바꾸는 방법이 있는지 여부 확인
    - 문자열 뒤에 A를 추가
    - 문자열 뒤집고 뒤에 B를 추가
S에서 T로 바꾸는데 2가지 방법 모두 '추가'이다.
    -> S는 T보다 작다
    -> 작은 것에서 큰 것을 만드는 데 있어서 많은 경우의 수가 있지만 반대로
    큰 값에서 작은 값으로 만드는 데는 간단하다(제한 조건을 반대로 적용)

문자열 뒤에 A를 추가한다 -> 문자열 뒤에 A가 있으면 제거한다
문자열을 뒤집고 B를 추가한다 -> 문자열 뒤에 B가 있으면 제거하고 뒤집는다.

>> 코드
dfs 로 풀이 할 것
    - 전제조건 : 기저조건이 필요함 -> len(t)와 len(s)가 같을 때!
    - 로직 : 
        1) if str_t[-1] == 'A' then pop() & call()
        2) if str_t[-1] == 'B' then pop() & reverse() & call()

'''


def dfs(tmp_t: str) -> int:
    ret = 0

    if len(tmp_t) == len(S):
        if tmp_t == S:
            ret = 1
        return ret

    if tmp_t[-1] == 'A':
        tmp_t.pop()
        ret = dfs(tmp_t)
        tmp_t.append('A')

    if tmp_t[-1] == 'B':
        tmp_t.pop()
        tmp_t = tmp_t[::-1]
        ret = dfs(tmp_t)
        tmp_t = tmp_t[::-1]
        tmp_t.append('B')

    return ret


if __name__ == '__main__':
    S, T = [list(input()) for _ in range(2)]

    print(dfs(T))
