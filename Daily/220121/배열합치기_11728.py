'''
>> P
정렬된 배열 A,B를 합친 뒤 정렬 후 출력하라
    - 범위 -> 크기 : ~ 100만    // 값 : ~ 10억 
>> S
범위가 크니까 O(N**2)는 어렵고 O(NlogN)인데...
1. 그냥 sort()하면 시간 초과 나나?


'''

N, M = tuple(map(int, input().split()))
A = list(map(int, input().split()))
A.extend(list(map(int, input().split())))

print(*sorted(A))
