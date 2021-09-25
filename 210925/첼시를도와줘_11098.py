

for _ in range(int(input())):
    # lst = []
    # for i in range(int(input())):
    #     lst.append(list(map(str, input().split())))
    lst = [input().split() for _ in range(int(input()))]
    # print(sorted(lst, key=lambda x: int(x[0])).pop()[1])
    print(max(lst, key=lambda x: int(x[0]))[1])
