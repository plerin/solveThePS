'''
> P
크기가 N인 수열이 있고 각 원소 Ai에 대해 오큰수 NEG(i)를 구하려고 한다. 
    - 오른쪽에 있으면서 Ai보다 큰 수 중 가장 왼쪽에 있는 수 // 없으면 -1 반환
> S
접근
    1. 이진탐색 라이브러리 써서 시간 복잡도 O(NlogN) 으로 풀이 가능 
        - from bisect import left/right -> for 문으로 돌면서 슬라이스한 binary_search([i:],i) -> 함수는 있으면 +1 없으면 -1 리턴
        -> 아 맞다 이진탐색 조건이 정렬되있어야 해...
    2. stack과 tuple 활용 _ 
        1) ret = [-1] * len()
        2) for문으로 돌아가며 stack에 넣고 stack에 값이 있으면 현재 값과 비교해서 현재값보다 작으면 pop하고 ret의 idx 순서에 현재 값 입력 
'''

A = int(input())
seq = list(map(int, input().split()))
stack = []
ret = [-1] * len(seq)

# for i in range(len(seq)):
#     while stack and stack[-1][0] < seq[i]:
#         val, idx = stack.pop()
#         ret[idx] = seq[i]
#     stack.append((seq[i], i))


for i in range(len(seq)):
    while stack and seq[stack[-1]] < seq[i]:
        # val, idx = stack.pop()
        ret[stack.pop()] = seq[i]
    stack.append(i)

print(*ret)
