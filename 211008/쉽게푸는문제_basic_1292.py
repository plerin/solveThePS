'''
goal : 특정 수열에서 A,B번째 숫자까의 합 구하기
1. 입력 받기
    1) A,B : 둘다 INT
로직
    1) 규칙에 맞게 수열 리스트에 담는다.
    2) slicing으로 자른다.
'''

#!
A, B = list(map(int, input().split()))

# 2
seq, cnt = [], 1
while len(seq) < B:
    seq.extend([cnt for _ in range(cnt)])
    cnt += 1
# 3
print(sum(seq[A-1:B]))
