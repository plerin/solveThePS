'''
> P
N개의 수로 이뤄진 수열이 있고 i부터 j번째 수까지의 합이 M이 되는 경우 구하라
> S
투 포인터 풀이
bruteforce로 푼다면 시간 제한을 못 맞춰 -> O(N**2)
투 포인터 풀이 시간 복잡도 -> O(N)
두 방법 모두 풀이해보기
'''
# brute_force

# two pointer
def numberOfCase(n, m):
    global data
    end = 0
    interval_sum = 0
    cnt = 0

    for start in range(n):
        while interval_sum < m and end < n:
            interval_sum += data[end]
            end += 1

        if interval_sum == m:
            cnt += 1

        interval_sum -= data[start]

    return cnt


n, m = map(int, input().split())
data = list(map(int, input().split()))

ret = numberOfCase(n, m)

print(ret)
