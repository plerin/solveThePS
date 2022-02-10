'''
> P
queue 자료구조에서 어떤 한 문서가 몇 번째 인쇄되는지 알아내는 프로그램 작성
    - 규칙1. 중요도를 확인
    - 2. 현재 문서보다 중요도가 높은 문서가 하나라도 있으면 queue 맨 뒤로 재배치
> S
구현 _ 자료구조(queue)
    1. deque 활용 _ queue _ (값,현재인덱스)
    2. popleft() -> if max()값이면 추출(cnt+=1) / else append()
    3. 만약 max()값의 인덱스가 내가 찾던 값이면 끝
'''

from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque([(i, v) for i, v in enumerate(arr)])

    while queue:
        max_v = max(queue, key=lambda x: x[1])[1]
        i, v = queue.popleft()

        if v == max_v:
            if i == m:
                break
        else:
            queue.append((i, v))

    print(len(arr)-len(queue))
