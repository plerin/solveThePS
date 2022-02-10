'''
[P]
N개의 원소를 포함하는 오름차순 정렬된 수열에서 X의 개수를 구해라
    - 시간 복잡도는 O(logN)으로 설계하라
    - N의 범위는 1백만, X의 범위는 10의 9승
[S]
정렬된 수열 & 큰 범위 & 시간 복잡도(logN)=> 이진 탐색 냄새 맡아라
    - 유형 : 이진 탐색 _ 표준 라이브러리 사용
[L]
이진 탐색 라이브러리 사용하여 간단히 해결
from bisect import bisecf_left, bisect_right
'''

from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
array = list(map(int, input().split()))

ret = bisect_right(array, x) - bisect_left(array, x)

if ret == 0:
    print(-1)
else:
    print(ret)
