
N,X = map(int,input().split())

ret = list(filter(lambda x: x < X,map(int, input().split())))
print(*ret)
# print(list(map(lambda x: int(x) if int(x) < X else 0, input().split())).)