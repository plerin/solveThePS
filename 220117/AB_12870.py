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


풀이
1. 패턴을 찾아라
개수를 임의로 설정해서(N) A가 어떻게 변하고 언제 추가하는지?
    - A가 추가되는 경우 / A가 앞으로 밀리는 경우가 있다.
    -> A가 맨 앞으로 밀리면 그 다음은 A가 추가되는데 이 때 앞 자리 A 개수에 따라 영향을 받음
        ex) AABBBB -> AAABBB 인 이유는 현재(8)에서 다음은(9)인데 이 때 필요한 B는 1개지만 B->A가 변함으로 써 앞의 A 2개는 B를 1개씩 잃어서 필요한 B의 개수가 3개가됨
2. 코드로 풀이
    1) ['B']로 초기화
    2) a개, 현재 k개수, a 인덱스를 사용하여 코드로 풀이
    3) 현재 k가 원하는 K보다 작은 경우 반복
    4-1) 추가한 a가 가장 앞으로 왔을 때(더 이상 앞으로 밀지 못하고 새로운 a를 추가해야하는 경우)last_index <= a_count - 1
        [N-1-(a_count+1)] 위치에 'A' 갱신
    4-2) a를 앞으로 밀어주면 ㅗ디는 경우
        [last_index] = 'B' , [last_index-1] = 'A'
        last_index -= 1 and cur_k += 1
    5) 반복문이 끝났을 때 K와 같으면
'''


def getStr(N: int, K: int) -> str:
    curStr = ['B'] * N  # 초기값 B로 초기화
    a_count = 0  # a 개수
    cur_k = 0   # 현재 K개수 == (i,j)쌍
    last_index = -1  # a index

    while cur_k < K:    # 현재 쌍의 개수가 K보다 작을 때
        if last_index <= a_count - 1:  # a 인덱스가 가능한 앞에 있어서 a를 추가해야 하는 경우
            if curStr[N-1-(a_count+1)] == 'A':
                break
            else:
                # acount+1인 경우는 a 개수에 따라 인덱스 위치가 변경됨(앞에 a가 2개 있으면 뒷자리에 a를 추가했을 때 앞자리 a의 b 개수가 줄어드니까!)
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
