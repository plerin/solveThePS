'''
> P
1~N까지 수를 사전순으로 출력하시오

> 접근
1. from itertools import permutations
2. 다음 순열 로직 사용 
3. DFS 백트래킹 사용

직관성
1 -> 3 -> 2
'''


from itertools import permutations


# def totPermutation(N: int):
#     seq = [i for i in range(1, N+1)]
#     x, y = 0, 0
#     print(*seq)
#     while seq != sorted(seq, reverse=True):
#         for i in range(N-1, 0, -1):
#             swap = False
#             if seq[i-1] < seq[i]:
#                 x, y = i-1, i

#                 for j in range(N-1, 0, -1):
#                     if seq[j] > seq[x]:
#                         seq[x], seq[j] = seq[j], seq[x]
#                         seq = seq[:y] + sorted(seq[y:])
#                         swap = True
#                         break

#             if swap == True:
#                 print(*seq)
#                 break


def totPermutation(part: list):
    global N

    if len(part) == N:
        print(*part)
        return

    for num in range(1, N+1):
        if num in part:
            continue
        part.append(num)
        totPermutation(part)
        part.pop()


N = int(input())

totPermutation([])

# for perm in ans:
#     print(*perm)
# totPermutation(N)

# for perm in permutations(range(1, N+1), N):
#     print(*perm)
