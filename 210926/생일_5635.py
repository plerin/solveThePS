
grp = [input().split() for _ in range(int(input()))]
grp.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(grp[-1][0], grp[0][0], sep='\n')
