N = int(input())
nums = list(set(map(int, input().split())))

print(*sorted(nums))
