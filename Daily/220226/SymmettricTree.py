'''
>> P
이진트리(root)가 mirror 형태인지 확인
    - 재귀 / 반복 형태로 풀어라
>> S

재귀
자식 노드(l,r)가 모두 있을 때와 없을 때로 구분
1. self.dfs(root.left, root.right) 호출
2. dfs 함수
def dfs(self, l, r):
    if l and r:
        return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
    return l == r

반복
stack에 l,r 담아놓고 반복
stack = [(root.left, root.right)]

while stack:
    l, r = stack.pop()
    if not l and not r:
        continue
    if not l or not r or (l.val != r.val):
        return False
    stack.append((l.left, r.right))
    stack.append((l.right, l.left))
    
return True

복잡도
시간 : O(n)
공간 : O(N)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dfs(self, l, r) -> bool:
        if l and r:
            return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
        return l == r

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)
