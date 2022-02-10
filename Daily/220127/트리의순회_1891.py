'''
>> P
1~n까지 숫자가 적힌 정점으로 이루어진 이진 트리가 있다.
인오더, 포스트오더가 주어질 때 프리오더 구하는 프로그램

>> S
인/포스트 오더 규칙으로 인오더를 찾아야 함
포스트 오더는 parent가 뒤에 있고 인오더는 parent가 중간에 있어 왼쪽 / 오른쪽 서브트리를 구분함

접근
1. 인오더 값에 따른 위치(index) 저장
2. 포스트오더 parent를 구해 parent 출력
3. left와 right를 구함
4. 프리오더 규칙처럼 왼쪽/오른쪽 서브트리 재귀호출

코드
1. 위치 저장
position = [0] * (n+1)
for i in range(n):
    position[inorder[i]] = i
2. parent 구하기
parent = post_order[post_end]
print(parent)
3. left, right 구함
left = left_start + position[parent]
right = left_end - position[parent]
4. 재귀호출
solve(in_start, left-1, post_start, 
solve(right))
'''