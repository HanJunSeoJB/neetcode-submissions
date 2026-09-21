# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        answer = True

        def dfs(node):
            nonlocal answer
            if node is None:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if abs(left_height - right_height) > 1:
                answer = False

            return max(left_height, right_height) + 1

        dfs(root)
        return answer


            