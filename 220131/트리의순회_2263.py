'''
>> P
숫자 1~n이 적힌 정점을 갖는 이진트리가 있고
인오더와 포스트오더가 주어졌을 때 프리오더를 구하는 프로그램 작성
    - 번호에 중복은 없다.
>> S
in/post/pre order의 특징을 통해 규칙을 찾아내자

in_order : LPR _ 왼쪽 탐색 후 부모 그리고 오른쪽 탐색 
post_order : LRP _ 왼쪽 / 오른쪽 탐색 후 부모 탐색
pre_order : PLR _ 부모 먼저 탐색 후 왼쪽 / 오른쪽 순서

접근
post를 통해 root(parent)을 구하고 in에서 parent 위치를 알아내서 left와 right 서브 트리를 구분한다
pre는 PLR 이기 때문에 print(parent)하며 L,R 서브 트리를 재귀 호출

코딩
1. 입력 받기 
n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

2. in_order 값 위치 구하기
pos = [0] * (n+1)
for i in range(n):
    pos[in_order[i]] = i

3. 재귀 호출
    - param : (in_start, in_end, post_start, post_end)
solve(0, n-1, 0, n-1)

4. 메소드 구현
def solve(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    parent = post_order[post_end]
    pritn(parent)

    left = in_start + pos[parent]
    right = in_end - pos[parent]

    solve(in_start, in_start+left-1, post_start, post_start+left)
    solve(right, in_end, right, post_end-1)
'''
import sys
sys.setrecursionlimit(10**6)


def solve(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    parent = post_order[post_end]
    print(parent, end=' ')

    left = pos[parent] - in_start   # 왼쪽 노드 갯수
    right = in_end - pos[parent]    # 오른쪽 노드 갯수

    # in/post_end에서 -1한 이유 = parent 제외
    solve(in_start, in_start+left-1, post_start, post_start+left-1)
    solve(in_end-right+1, in_end, post_end-right, post_end-1)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pos = [0] * (n+1)
for i in range(n):
    pos[in_order[i]] = i


solve(0, n-1, 0, n-1)
