'''
> P
n개 자연수 중 길이가 m인 수열 모두 구하라
    - 중복되는 건 1개만 처리
    - 오름차순 출력

> kp
1. 중복되는 수열은 여러 번 출력 할 수 없다.
    -> 이전 출력 값을 저장해 놓아야 해

계속 시간 초과 나와서 다른 사람 풀이 참고
1. list & if 조합이 너무 느리니 hash 를 사용하여 중복 체크
    - if len(seq) == M then if seq in dic then return else dic[s] = 1 & print(seq)

2. permutations으로 조합 구하고 set으로 중복 제거
    - permutation(n,m) -> convert to list -> cover the set() -> return result
'''


from itertools import permutations


def findSeq(N: int, M: int, seq: str):
    global tot_seq, dic, visit

    if len(seq.split()) == M:
        if seq not in dic:
            dic[seq] = 1
            print(seq)
        return

    for idx in range(len(tot_seq)):
        if visit[idx] == True:
            continue
        visit[idx] = True
        findSeq(N, M, seq + str(tot_seq[idx]) + ' ')
        visit[idx] = False


N, M = map(int, input().split())
tot_seq = list(map(int, input().split()))
visit = [False for _ in range(N)]   # 꼭 필요 9, 9 같은 경우 잡아주기 위해서
dic = {}    # if + list 찾는거보다(O(n)) hash가(O(1)) 훨씬 빠르다!

# tot_seq.sort()

# findSeq(N, M, '')

perm = permutations(tot_seq, M)

for perm in sorted(set(permutations(tot_seq, M))):
    print(*perm)
