
# ret = []

ret = [list(map(int,input().split())) for _ in range(int(input()))]
print(sum(map(lambda x: x[1]%x[0], ret)))
# for _ in range(int(input())):
#     a, b = map(int,input().split())
#     ret.append(b%a)
    # ret.append(int((map(lambda x: int(x[0])%int(x[1]), input().split()))))

# print(sum(ret))
print(ret)