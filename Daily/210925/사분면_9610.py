
# ret = [0 for _ in range(5)]

# for _ in range(int(input())):
#     x, y = map(int, input().split())

#     if x > 0 and y > 0:
#         ret[0] += 1
#     elif x < 0 and y > 0:
#         ret[1] += 1
#     elif x < 0 and y < 0:
#         ret[2] += 1
#     elif x > 0 and y < 0:
#         ret[3] += 1
#     else:
#         ret[4] += 1
# # print(list(map(lambda a: a[0], enumerate(ret))))
# an = list(map(lambda x: 'Q'+str(x[0]+1)+': '+str(x[1])
#               if x[0] < 4 else 'AXIS: '+str(x[1]), enumerate(ret)))
# for a in an:
#     print(a)


ret = [0 for _ in range(5)]

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a*b == 0:
        ret[4] += 1
    elif a*b > 0:
        ret[int(a+b < 0)*2] += 1
    elif a*b < 0:
        ret[int(a > b)*2+1] += 1

for i in range(4):
    print(f'Q{i+1}: {ret[i]}')
print('AXIS:', ret[4])
