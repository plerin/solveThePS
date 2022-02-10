T = int(input())
for _ in range(T):
    a = sorted(list(map(int, input().split())), reverse=True)
    print(a[2])
