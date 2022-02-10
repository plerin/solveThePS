'''
>> P
수열 A가 주어졌을 때 가잔 긴 증가 부분 수열 구하라
    - 길이를 구하라
>> S
다양한 방법으로 풀어보기
1. DP 이용 _ 길이
    - 시간 복잡도 : O(N^^2)
    - 점화식 : ai = i번째까지 기장 긴 부분 수열 길이
        d[i] = max(d[j]+1, d[i]), 단 i보다 작은 j 중 val 값이 작은 경우
        j = i 앞의 index 중 a[i]보다 a[j]가 작은 경우
        -> 내 코드를 더 간략하게 한 것

    - 풀이 : 
        1) 최대 값 선언 MAX = 1001
        2) dp 테이블 초기화(본인 값을 갖기에 1) _ dp = [1] * MAX
        3) 0~N만큼 탐색 -> 0~i만큼 탐색 -> if seq[j] < seq[i] -> dp[i] = max(dp[i], dp[j]+1) 
        4) dp 테이블 중 최대 값 반환 _ return max(dp)

2. 이진탐색 _ 라이브러리
    - 시간 복잡도 : O(NlogN) -> len(A)개 만큼 반복하며 이진 탐색하기 때문
    - 접근
        모든 원소를 탐색하며 해당 원소의 lower_bound를 찾아 입력
    - 풀이
        0) 라이브러리 선언 _ from bisect import bisect_left
        1) 빈 리스트 생성 _ part_seq = [0]
        2) 원소 탐색 _ for num in seq:
            1) 배열 값보다 큰 경우 if part[-1] < num then part.append(num)
            2) 작은 경우 -> 위치 찾아 replace함 
        3) return len(part)

3. 이진탐색 _ 로직 구현
4. 이진탐색 _ 길이 대신 부분 수열
'''
import sys
from bisect import bisect_left

input = sys.stdin.readline

MAX = 1001

# solve with bisect library


def use_library() -> int:
    part = [0]
    for num in seq:
        if part[-1] < num:
            part.append(num)
        else:
            pos = bisect_left(part, num)
            part[pos] = num
    return len(part) - 1    # remove index 0

# solve with bisect logic


def use_logic() -> int:
    part = [0]
    for num in seq:
        if part[-1] < num:
            part.append(num)
        else:
            left, right = 0, len(part)

            while left < right:
                mid = (left + right) // 2
                if part[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            part[right] = num

    return len(part) - 1

# solve with dp


def solve() -> int:
    global dp
    ret = 0

    for i in range(N):
        for j in range(i):
            if seq[i] > seq[j]:  # 현재 값보다 작은 경우
                # dp[j] + 1  == 이전 dp 값에 현재 본인 값을 더한 값
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

    for i in range(N):  # 0 ~ N loop
        cur = 0
        for j in range(i):  # 0 ~ i loop then find large than me
            if seq[i] > seq[j]:
                cur = max(cur, dp[j])
        dp[i] = cur + 1
        ret = max(ret, dp[i])

    return ret


N = int(input())
seq = list(map(int, input().split()))

dp = [1 for _ in range(MAX)]    # 본인 포함하기 때문에 1로 초기화

ans = use_logic()

print(ans)
