# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        t1 = []
        t2 = []

        def dfs(node, arr):
            if node is None:
                arr.append("null")
                return
            
            arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)

            return arr
        
        t1 = dfs(p, t1)
        t2 = dfs(q, t2)

        if t1 == t2:
            return True

        return False