'''
>> P
N과 K가 주어졌을 때 두 조건을 만족하는 문자열 S를 찾아라
    - S 길이는 N이고 'A','B'로 이루어짐
    - i < j 이면서 s[i] == A && s[j] == B 를 만족하는 (i,j)쌍이 K개 있다.
    - 출력 조건 : S가 여러 개면 그 중 하나 출력 // 없으면 -1 출력
>> S
2번 조건을 만족하려면 A뒤에 B의 개수를 파악해야함 
    ex) AABBAB -> A[0] = 3 + A[1] = 3 + A[3] = 1 ==> 7
    - 5자리 중에 K개 가장 큰 경우는 ABBBB(X) ABABB(O)
K에 따라 앞에서부터 A로 채워나가기
    K >= N-1 -> A

K가 n-1보다 같거나 큰 경우와 작은 경우로 나누어 계산
    1) k >= N-1 -> 그 자리에 A
    2) k < N-1 -> 필요한 개수만큼 계산해서 해당 자리에 A 나머지 B
        ex) K=12, N=10이고 첫번째 자리에 A를 놓아서 K = 3, N = 9일 때 
        필요한건 3이지만 A를 놓으면 앞에서 9가 8이 되므로 필요한 수는 4
        앞에 A가 많으면 더 많이 깎여 
'''


def getStr(N: int, K: int) -> str:
    curStr = ['B'] * N
    a_count = 0
    cur_k = 0
    last_index = -1

    while cur_k < K:
        if last_index <= a_count - 1:
            if curStr[N-1-(a_count+1)] == 'A':
                break
            else:
                curStr[N-1-(a_count+1)] == 'A'
                last_index = N-1-(a_count+1)
                a_count += 1
                cur_k += 1
        else:
            curStr[last_index] = 'B'
            curStr[last_index-1] = 'A'
            last_index -= 1
            cur_k += 1

    if cur_k == K:
        return curStr
    else:
        return '-1'


N, K = map(int, input().split())
print(''.join(getStr(N, K)))
