'''
[P]
배열 A와 배열 B는 N개의 원소로 구성, K번 바꿔치기해서 만들 수 있는 배열 A의 모든 원소의 합
    - 최대 K번인거 보니 바꿔치기 횟수가 남아도 손해면 안 바꿈
[S]
정렬(SORT)

[L]
1. K번 동안 배열 A의 작은 값이 배열 B의 큰 값보다 작으면 교체
    - 교체 횟수가 남아도 A의 MIN 값이 B의 MAX 값보다 크면 교체X
'''

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(K):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
