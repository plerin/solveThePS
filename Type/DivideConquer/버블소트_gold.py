'''
backjoon url -> https://www.acmicpc.net/problem/1377

>> Keyword


>> P
버블 소트 알고리즘을 C++로 작성했다.
N = 배열크기, A = 정렬해야하는 배열, 인덱스는 1부터 시작
어떤 값이 출력되는지 구하라
    - 범위 : N < 50만보다 작거나 같은 자연수  // 값 < 100만보다 작거나 같은 자연수(0포함)

>> 버블 소트 알고리즘 풀이
N = 3일 때, 인덱스 1,2,3 사용
i = 1, j = 1~2반복, 1과 2 & 2와 3 정렬
i = 2, j = 1만 반복, 1과 2정렬
i = 3, 반복 없이 결과 출력

>> S
다른 사람의 접근 방법을 보고 정리함

정렬 전과 후에 대해 배열 값의 인덱스의 변화를 통해 정렬에 필요한 이동 횟수를 알 수 있음!
    - 예를 들면
    정렬 전 : 4,3,2 -> (4,0), (3,1), (2,2) 
    정렬 후 : 2,3,4 -> (4,2), (3,1), (2,0) 
    인덱스의 차(후 - 전)중 최대값을 구하고 +1를 하면 최대 이동횟수(정렬) = -2, 0, 2 => 3(2+1)

코드
1. 배열을 입력 받음 
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input().rstrip()) for _ in range(n)]

2. 배열의 인덱스 구하기
origin_ord = [(v,i) for i, v in enumerate(arr)]

3. 정렬 배열 인덱스 구하기
sort_ord = [(v,i) for i, v in enumerate(sorted(arr))]

4. 2,3 튜플 배열 차 중 가장 큰 값을 구하기
print(max([ sort_ord[i][1] - origin_ord[i][1] for i in range(n)]))

시간복잡도 : O(NlogN)
공간복잡도 : O(N)

'''

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = [int(input().rstrip()) for _ in range(n)]

origin_ord = defaultdict(int)
for i, v in enumerate(arr):
    origin_ord[v] = i

sort_ord = defaultdict(int)
for i, v in enumerate(sorted(arr)):
    sort_ord[v] = i

print(max([origin_ord[v] - sort_ord[v] for v in arr])+1)


# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = []
# for i in range(n):
#     arr.append((int(input()), i))

# sorted_arr = sorted(arr)
# answer = []


# for i in range(n):
#     print(arr[i], sorted_arr[i])
#     answer.append(sorted_arr[i][1] - arr[i][1])

# print(max(answer) + 1)
