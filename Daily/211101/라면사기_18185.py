'''
[P]
N개의 공장이 있는데 1번부터 n번까지 차례대로 번호가 붙어있을 때 최소 비용으로 라면 구매하고 그 비용 출력
    - i번 공장 => 3원
    - i번 공장 + (i+1)번 공장 => 5원
    - i번 공장 + (i+1)번 공장 + (i+2)번 공장 => 7원
[S]
최소 비용 + 라면 구하는 경우 3개 중 맨 밑부터 올라가며 이득 
    - 유형 : 그리디 알고리즘
    - 정당성 : 라면 구매 방법 3개 중 3->2->1 순으로 효율적이다 (최적의 해)
[L]
1. 풀이법
    - 공장별 라면 구매 개수를 stack에 넣고 다음 값이 '0'인지 아닌지에 따라 비용 갱신
'''

N = int(input())
costs = list(map(int, input().split()))

ret = 0
stack = []
for c in costs:
    if c == 0:
        ret = len(c)*2+1
        c = []
        continue
    if len(c) == 3:
