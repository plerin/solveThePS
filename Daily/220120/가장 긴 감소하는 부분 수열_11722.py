'''
>> P
수열 A가 주어졌을 때 가장 긴 감소하는 부분수열을 구하라
>> S
LIS <-> LDS겠네 Decrease 사용해서.
풀이는 LIS와 같지 않을까? 
로직은 그대로 사용해서 풀어보자

1. DP 활용
    - 시간 복잡도 : O(N^^2)
    - 점화식 :
        ai = i번째 값에서 가장 긴 감소 부분 수열 개수
        d[i] = max(d[i], d[j] + 1) 단, j는 i보다 작은 인덱스이며 val 값이 큰 경우에 한함
    - 접근
        1) MAX 값 선언
        2) dp 테이블 생성 _ dp = [1] * MAX _ 본인 자신을 갖고있어서 1로 초기화
        3) for with 0 ~ N -> for with 0 ~ i -> if seq[i] < seq[j] then dp[i] = max(dp[i], dp[j] + 1) 
        4) return max(dp)

2. upper_bound 활용
    - 시간 복잡도 : O(N logN)
    - 접근 : do not use library but do logic
        1) 리스트 선언(기본 값 갖고있도록) _ arr = [0]
        2) for with seq -> if arr[-1] < num then append else
            left, right = 0, len(part)
            while left < right:
                mid = + // 2
                if [mid] < num then left = mid + 1
                else then right = mid
            [right] = num
        3) return len(part)
'''
from bisect import bisect_left, bisect_right


def use_dp() -> int:
    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if seq[i] < seq[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def use_logic() -> int:
    part = [1e9]

    for num in seq:
        if part[-1] > num:
            part.append(num)
        else:
            left, right = 0, len(part)

            while left < right:
                mid = (left + right) // 2

                # mid 보다 num이 크면 left가 당겨져 == 중간 값이 새로 들어온 값이 크면 left를 당겨 == 왜냐하면 replace해야 할 대상이 오른쪽에 있는거니까
                if part[mid] > num:
                    left = mid + 1
                else:
                    right = mid
            # print(left, right, num, part)
            part[right] = num
        # print(part)
    return len(part) - 1


def use_library() -> int:
    # bisect_left() = 오름차순일 경우 해당 값의 가장 왼쪽 index를 찾아줌
    # 위 문제는 내림차순이기 때문에 bisect_left()를 사용하려면 음수로 만들어야 함
    total = [i * (-1) for i in seq]
    part = [total[0]]
    for num in total:
        if part[-1] < num:
            part.append(num)
        else:
            pos = bisect_left(part, num)
            part[pos] = num

    return len(part)


N = int(input())
seq = list(map(int, input().split()))

# ans1 = use_dp()
# ans2 = use_logic()
ans3 = use_library()
# print(ans1, ans2)
print(ans3)
