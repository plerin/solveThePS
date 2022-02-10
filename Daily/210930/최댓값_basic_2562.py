import sys
ret = [int(input()) for _ in range(9)]

print(max(ret), ret.index(max(ret))+1, sep='\n')
