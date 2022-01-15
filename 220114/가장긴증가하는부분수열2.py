'''
>> P
수열 A가 주어졌을 때 가장 긴 증가 부분 수열 길이를 구하라
    - 범위 : 수열의 크기 / 값 => ~100만
>> S
수열을 구하는 게 아니라 길이를 구하는 것
시간 제한(1초)와 범위(~100만)는 O(N) 또는 O(NlogN) 알고리즘을 사용해야 함

- 한 칸씩 이동(L->R)하면서 이전 보다([-1]) 크면 APPEND 작으면 REPLACE
    - replace 기준은 이분탐색(O(logN))을 활용하여 mid값을 구하고 그 값을 대신함

>> C
1. 입력 값 변수에 저장
n = int(input())
A = list(map())

2. [0]인 리스트 생성 _ 부분 수열 담기 위함
part = [0]

3. A를 문자단위로 반복하며 part와 비교하며 append / replace
ans = solve()

print(ans)

4. 로직 함수
def solve() -> int:
    global part
    
    for c in A:
        if part[-1] < c:
            part.append(c)
        else:
            left, right = 0, len(part) - 1
            pos = 0
            while left <= right:
                mid = (left + right) // 2
                if part[mid] < c:
                    left = mid + 1
                elif part[mid] > c:
                    right = mid -1
                else:
                    pos = mid
            part[pos] = c
    return len(part) - 1 # 초기값 [0] 제외
'''
import sys

input = sys.stdin.readline


def solve():
    part = [0]

    for c in A:
        if part[-1] < c:
            part.append(c)
        else:
            left, right = 0, len(part)

            while left < right:
                mid = (left + right) // 2
                if part[mid] < c:
                    left = mid + 1
                else:
                    right = mid

            part[right] = c

    return len(part) - 1


N = int(input())
A = list(map(int, input().split()))

ans = solve()

print(ans)
