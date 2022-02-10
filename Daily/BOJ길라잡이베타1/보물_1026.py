'''
> P
길이 N개인 배열 A와 B가 있을 때 S의 최솟 값을 출력하라
    - S = A[0]*B[0] +... + A[N-1]*B[N-1]
    - A만 순서를 바꿀 수 있다.
> S
B의 큰 수에 A의 작은 수를 매칭하면 됨
B를 리스트로 담고 정렬한 뒤 B의 값을 통해 인덱스를 구해 A 값을 매칭하기
1. A/B 오름차순 정렬 
2. B를 반복하며 그 값과 매칭되는 인덱스에 해당하는 A의 값을 구함
3. b와 a가 매칭된 리스트를 zip으로 묶어 계산
'''

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# sort_A = sorted(A, reverse=True)
# sort_B = sorted(B)

# ret = []

# for i in B:
#     idx = sort_B.index(i)
#     sort_B[idx] = -1
#     ret.append((sort_A[idx], i))

# print(sum(map(lambda x: x[0]*x[1], ret)))

# a를 오름차순 정렬하고 가장 작은 a값과 가장 큰 b값의 곱을 ret에 중첩해서 더해줘
# b에서 가장 큰 값을 빼는 방법은 b의 가장 큰 값(max(b))를 찾고 해당 인덱스를 구해 pop()을 해주면 됨!
A.sort()
ret = 0
for i in range(N):
    a = A[i]
    b = B.pop(B.index(max(B)))
    ret += a*b

print(ret)
