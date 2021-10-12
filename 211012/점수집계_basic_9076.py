
T = int(input())

for _ in range(T):
    scores = sorted(list(map(int, input().split())))
    if scores[3] - scores[1] >= 4:
        print('KIN')
    else:
        print(sum(scores[1:4]))
