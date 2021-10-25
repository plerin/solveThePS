'''
P
N이 1될 때까지 2가지 과정을 수행하는 최소 횟수
    1. N -= 1
    2. N //= K
S
1. 그리디 알고리즘 _ K로 나누고 못 나눌 경우 1을 빼기를 반복
    정당성 : 어떠한 경우에서도 나누는 경우가 1을 빼는 것보다 효율적이다(또한 N은 항상1에 도달!) ==> 최적의 해 성립
L
1. 함수 이용
    PARAM : N(INT),K(INT)
    LOGIC : N//=K if N%K == 0 else N-=1
    RETURN : count
'''

# 횟수마다 나눌 수 있는 값인지 체크 => 연산이 많음
# def untilOne(n, k):
#     cnt = 0

#     while n != 1:
#         n = n//k if n % k == 0 else n-1
#         cnt += 1

#     return cnt


# N, K = map(int, input().split())
# ret = 0

# ret = untilOne(N, K)

# print(ret)

# 한 번 나눌 때마다 나누어 떨어지는 수를 구함 => 연산이 줄음
n, k = map(int, input().split())

ret = 0

while True:
    # N이 k로 나누어 떨어지는 수가 될 때가지 빼기
    target = (n // k) * k
    ret += (n-target)
    n = target
    # N이 K보다 작을 때 반복문 탈출
    if n < k:
        break
    # K로 나누기
    ret += 1
    n //= k

# 남은 수 에서 1씩 빼기(1 만들기)
ret += (n-1)
print(ret)
