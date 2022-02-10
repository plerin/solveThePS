'''
> P
골드바흐 추측 : 2보다 큰 짝수는 두 소소의 합으로 나타낼 수 있다.
짝수(N)이 주어졌을 때 골드바흐 파티션 개수 구하자
> S
수학
> L
    1. 입력 값의 MAX값을 구하고 MAX까지의 리스트 중 소수를 미리 구해 -> 테스트 케이스마다 소수 안 찾기 위해
    2. 2부터 MAX값 까지 반복하며 합이 N이 되는 경우 카운트+=1
    3. 결과 출력
'''
import sys

# input = sys.stdin.readline
# MAX = 1000001


# def findPrime():
#     check = [True] * MAX

#     for i in range(2, int(MAX**0.5)+1):
#         if check[i] == True:
#             for j in range(i*i, MAX, i):
#                 check[j] = False
#     return check


# is_prime = findPrime()

# for _ in range(int(input())):
#     n = int(input())
#     ret = 0
#     for i in range(2, n//2+1):
#         if is_prime[i] == True and is_prime[n-i] == True:
#             ret += 1
#     print(ret)


t = int(input())
nums = [int(input()) for _ in range(t)]

MAX = max(nums)+1


def findPrime():
    check = [True] * MAX

    for i in range(2, int(MAX**0.5)+1):
        if check[i] == True:
            for j in range(i*i, MAX, i):
                check[j] = False
    return check


is_prime = findPrime()

for n in nums:
    ret = 0
    for i in range(2, n//2+1):
        if is_prime[i] == True and is_prime[n-i] == True:
            ret += 1
    print(ret)
