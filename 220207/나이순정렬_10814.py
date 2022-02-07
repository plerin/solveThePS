'''
>> P
나이와 이름이 순서대로 주어질 때 
나이 증가, 앞에 오는 순서대로 정렬하여 출력

>> S

접근
입력 받을 때 순서도 같이 저장하고 이를 활용하여 정렬

코딩
import heapq

N = int(input())
arr = []

for i in range(N):
    age, name = input().split()
    heapq.heappush(arr, (int(age), i, name))

while arr:
    age, idx, name = heapq.heappop(arr)
    print(age, name)
'''

import heapq

N = int(input())
arr = []

for i in range(N):
    age, name = input().split()
    heapq.heappush(arr, (int(age), i, name))

while arr:
    age, idx, name = heapq.heappop(arr)
    print(age, name)
