'''
>> P
N,K가 주어졌을 때 조건을 만족하는 S를 찾는 프로그램 작성
    - S의 길이는 N이고 'A','B'로 이루어져있다.
    - i < j 이며 s[i] == 'A' && s[j] == 'B'를 만족하는 (i,j)쌍이 K개가 있다.
>> S
a와 b에 따라 K쌍의 상관관계를 구하자
bbbbb -> 0개
bbbab -> 1개
bbabb -> 2개
babbb -> 3개
abbbb -> 4개
그 다음은 ..?
ababb -> 5개 -> 이 때 b가 1개가 필요함에도 [2]에 a가 들어간 이유는 [0]이 a이기 때문에 b->a로 바뀌며 -1 하기 때문
aabbb -> 6개

패턴은 크게 a가 앞으로 밀리는 연산과 a개 새롭게 들어가는 연산으로 나뉨
그럴 때마다 현재 만족하는 쌍의 개수는 +1 

>> C
초기 문자열 초기화 -> ['B'] * N
a 개수 -> aCount(int) = 0
a index -> lastAIndex(int) = -1(없으니까)

def getStr(N: int, K: int) -> str:
    str = ['B'] * N
    a_count = 0
    last_index = -1
    cur_k = 0

    while cur_k < K:
        if last_index <= a_count - 1:
            if str[N-1-(a_count+1)] != 'A':
                break
            else:
                str[N-1-(a_count+1)] = 'A'
                last_index = N - 1 - (a_count+1)
                a_count += 1
                cur_k += 1 
        else:
            str[last_index] = 'B'
            str[last_index-1] = 'A'
            last_index -= 1
            cur_k += 1
    
        if cur_k == K:
            return ''.join(str)
        else:
            return '-1'
'''


def getStr(N: int, K: int) -> str:
    str = ['B'] * N     # 문자열 초기화
    a_count = 0         # A 개수
    last_index = -1     # 마지막 A 인덱스
    cur_k = 0           # 현재 (i,j) 쌍 개수

    while cur_k < K:
        if last_index <= a_count - 1:   # 마지막 A인덱스가 최대한 앞으로 밀렸을 때 == 새로운 A 입력
            if str[N-1-(a_count+1)] == 'A':  # 해당 자리에 이미 A가 있을 때 _ 해당 자리수(N)에서 더이상 K를 얻지 못할 때
                break
            else:
                str[N-1-(a_count+1)] = 'A'
                last_index = N - 1 - (a_count+1)
                a_count += 1
                cur_k += 1
        else:
            str[last_index] = 'B'
            str[last_index-1] = 'A'
            last_index -= 1
            cur_k += 1

    if cur_k == K:
        return ''.join(str)
    else:
        return '-1'


N, K = map(int, input().split())
print(getStr(N, K))
