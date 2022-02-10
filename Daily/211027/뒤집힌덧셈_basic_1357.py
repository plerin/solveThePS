x, y = map(str, input().split())
ret = str(int(x[::-1])+int(y[::-1]))[::-1]
print(int(ret))
