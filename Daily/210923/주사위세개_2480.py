def dice(inp):
    inp.sort()
    dup = len(set(inp))

    if dup == 1: return 10000+inp[0]*1000
    elif dup == 2: return 1000+inp[1]*100
    else: return inp[2]*100
    

f,s,t = map(int,input().split())

ret = dice([f,s,t])

print(ret)


# 이런 풀이도 가능
# a,b,c=sorted(list(map(int,input().split())))
# print([[c*100,1000+b*100][a==b or b==c],10000+1000*a][a==c])