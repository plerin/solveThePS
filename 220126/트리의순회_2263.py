'''
>> P
1~n 숫자를 갖는 정점이 n개인 이진트리가 있다.
인오더, 포스트오더가 주어졌을 때 프리오더 구하는 프로그램 작성

>> S
접근
1. 인/프리/포스트 오더 특징 알아보기
    - pre_order : PLR _ 부모 -> 왼쪽 -> 오른쪽  탐색
    - in_order : LPR _ 왼쪽 -> 부모 -> 오른쪽 탐색
    - post_order : LRP _ 왼쪽 -> 오른족 -> 부모 탐색
2. 인/포스트 오더 특징을 이용해 프리 오더 구하기
post를 통해서 in에서의 parent를 찾고 왼쪽/오른쪽 서브트리를 구분
pre_order = PLR 이니까 P(parent)출력하고 왼쪽/오른쪽 순서대로 서브트리 호출 == 재취호출

코드
1. 입력 받기
n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
2. 변수 선언
position = [0] * n+1 # in_order의 parent index 확인 위해

for num in range(n):
    position[in_order[i]] = i # val에 해당하는 index(위치) 저장

3. 함수 호출
solve(0, n-1, 0, n-1)

def solve(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    parent = post_order[post_end]
    print(parent)

    #left / right 구분
    left = in_end - position[parent] -1 
    right = in_start + postition[parent]


    solve(in_start, left, post_start, post_end-left)
    solve(right, in_end, post_start+right, post_end-1)

'''


def solve(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    parent = post_order[post_end]
    print(parent, end=' ')

    # left / right 구분 _ parent 중심으로 in_start, in_end와 연산
    left = position[parent] - in_start
    right = in_end - position[parent]

    # in_start + left - 1, post_start+left - 1(-1은 모두 중앙(parent) 제외)
    solve(in_start, in_start+left-1, post_start, post_start+left-1)
    # in_end-right+1(parent 제외==index이동) , post_end-1(맨 마지막 root 제외)
    solve(in_end-right+1, in_end, post_end-right, post_end-1)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

position = [0] * (n+1)

for i in range(n):
    position[in_order[i]] = i


solve(0, n-1, 0, n-1)
