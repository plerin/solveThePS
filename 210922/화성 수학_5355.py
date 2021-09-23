
def marsMath(in_lst):
    out_lst = []
    oper = {'@': '*3', '%': '+5', '#': '-7'}

    for expr in in_lst:
        cal = float(expr[0])
        for i in range(1, len(expr)):
            cal = eval(str(cal)+oper[expr[i]])
        out_lst.append(cal)
    return out_lst


N = int(input())
in_lst = []

for _ in range(N):
    in_lst.append(list(map(str, input().split())))

ret = marsMath(in_lst)
for v in ret:
    print('{0:0.2f}'.format(v))
