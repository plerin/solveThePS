'''
prime number 
def isPrimeNumber(x):
    for i in range(2,n):
        if x % i == 0:
            return False
    return True

-> time-complexity : O(X) _ x가 소수인지 확인하기 위해

제곱근 까지만 구하고 그 안에 약수가 있다면 약수가 있다는 의미
def isPrimeNumber(x):
    for i in range(2,(n**0.5)+1):
        if x % i == 0:
            return False
    return True

-> time-complexity : O(N**0.5)

에라토스테네스의 체 : 특정 범위 안의 자연수들의 소수를 구함 
    - 속도는 빠르지만 메모리를 그만큼 사용함


# 1 ~ 1000까지 소수 구하라 _ 에라토스테네스의 체 이용


def findPrime(n):
    prime = []
    visit = [False] * (n+1)

    for i in range(2, n+1):
        if visit[i] == True:
            continue

        prime.append(i)

        for j in range(i, n+1, i):
            visit[j] = True

    return prime


n = 100

ret = findPrime(n)

print(*ret)


투 포인터(Two Pointer) : 리스트에 순차적으로 접근해야할 때 두 개의 점의 위치를 기록하면서 처리(시작점과 끝점)



'''

# 문제 2. [1,2,3,2,5] 수열이 있고 총 합이 5인 경우를 구하라

# 완전탐색


def bruteForce(n, m):
    pass

# 투 포인터 _ start / end 를 사용하여 특정 리스트에서 시간복잡도를 줄이는 테크닉


def twoPointer(n, m):
    global data

    count = 0
    interval_sum = 0
    end = 0

    for start in range(n):
        while interval_sum < m and end < n:
            interval_sum += data[end]
            end += 1

        if interval_sum == m:
            count += 1

        interval_sum -= data[start]

    return count


n = 5
m = 5
data = [1, 2, 3, 2, 5]

ret = twoPointer(n, m)
print(ret)


n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left, right = 3, 4
print(prefix_sum[right] - prefix_sum[left-1])
