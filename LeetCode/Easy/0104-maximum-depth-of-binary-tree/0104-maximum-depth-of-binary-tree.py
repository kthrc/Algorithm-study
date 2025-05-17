import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 제공된 상태대로 안에서 함수 만들고 실행해야 함
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0

        # 예외 처리
        if root is None:
            return self.max_depth

        # 재귀
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # 루트 높이도 세야하기 때문에 +1 해줘야 함
        self.max_depth = max(left_depth, right_depth) + 1

        return self.max_depth