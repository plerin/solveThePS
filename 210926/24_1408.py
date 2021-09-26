time = [3600, 60, 1]
n = sum(map(lambda x: int(x[1])*time[x[0]], enumerate(input().split(':'))))
m = sum(map(lambda x: int(x[1])*time[x[0]], enumerate(input().split(':'))))

if n < m:
    diff = m-n
    h, r = divmod(diff, 3600)
    m, s = divmod(r, 60)
else:
    diff = ((24*3600)-n)+m
    h, r = divmod(diff, 3600)
    m, s = divmod(r, 60)

print('{0:02d}:{1:02d}:{2:02d}'.format(h, m, s))


# h1, m1, s1 = map(int, input().split(':'))
# h2, m2, s2 = map(int, input().split(':'))
# t = h2*3600+m2*60+s2 - (h1*3600+m1*60+s1)
# if t < 0:
#     t = t+ 60*60*24
# h = t//3600
# m = (t%3600)//60
# s = t%60
# print("%02d:%02d:%02d" % (h,m,s))
