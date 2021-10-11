N = int(input())
nums = list(map(int, input().split()))
ret = 1

for i in nums:
    ret *= i

print(ret)
