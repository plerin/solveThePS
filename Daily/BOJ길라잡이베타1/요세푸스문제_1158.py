'''
> P
1~N까지 N명이 사람이 원을 그리며 앉아있고 k번째 사람을 제고하는 식으로 모든 사람이 제거 될때까지 진행, 그렇나 만들어진 수열을 구하라
    - (N,K) 요세푸스 순열이라고 함
> S
구현 _ 규칙 찾기
    - 1~n까지 리스트에서 규칙에 해당하는 idx 값을 꺼내면 됨 
    - 규칙 : idx = (k-1)%len(arr)

'''

N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
ret = []
idx = 0
while arr:
    idx = (idx+(K-1)) % len(arr)
    ret.append(str(arr.pop(idx)))

print(f'<{", ".join(ret)}>')
