'''
> P
크기가 N인 수열 중 각 원소에 대해서 오등큰수를 구하려고 한다.
    - 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(A)보다 큰 수중 가장 왼쪽에 있는 수 // 없는 경우 -1
> S
접근
    - 수열(seq)를 Count로 각 숫자에 대한 횟수를 담아놓고
    - 오큰수 처럼 stack에 tuple 형식으로 (횟수,idx)를 담아놓고
    - 수를 반복하며 stack에 값이 있고 [-1][0] 보다 크면 뺀다 아니면 남아있어 어짜피 ret의 기본 값은 -1이니까
'''
from collections import Counter

A = int(input())
seq = list(map(int, input().split()))
cnt = Counter(seq)
stack = []
ret = [-1] * len(seq)

# for i in range(len(seq)):
#     while stack and stack[-1][0] < cnt[seq[i]]:
#         val, idx = stack.pop()
#         ret[idx] = seq[i]
#     stack.append((cnt[seq[i]], i))


for i in range(len(seq)):
    while stack and cnt[seq[stack[-1]]] < cnt[seq[i]]:
        ret[stack.pop()] = seq[i]
    stack.append(i)


print(*ret)
