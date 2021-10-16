# keypoint : deque를 이용해 학생 수와 점수를 분리한 후 round로 평균을 구한다

from collections import deque

for _ in range(int(input())):
    # lst = deque(list(map(int, input().split())))
    # n = lst.popleft()
    n, *lst = list(map(int, input().split()))
    avg = sum(lst)/n
    ret = len(list(filter(lambda x: x > avg, lst)))/n*100

    print('{idx:0.3f}%'.format(idx=ret))
