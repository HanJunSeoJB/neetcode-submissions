# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(node, count):
            nonlocal answer
            if node is None:
                answer = max(answer, count)
                return
            
            count += 1
            dfs(node.left, count)
            dfs(node.right, count)
        
        dfs(root, 0)

        return answer
