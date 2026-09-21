# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(node):
            nonlocal answer
            
            # 기저 조건: 노드가 없으면 높이는 0
            if not node:
                return 0
            
            # 왼쪽, 오른쪽 자식 트리의 높이를 각각 구함
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # 현재 노드를 꺾이는 지점으로 삼았을 때의 경로 길이(왼쪽 높이 + 오른쪽 높이)로 최댓값 갱신
            answer = max(answer, left_height + right_height)

            # 부모 노드에게는 현재 노드의 높이(왼쪽과 오른쪽 중 긴 것 + 1)를 반환
            return max(left_height, right_height) + 1

        dfs(root)
        
        return answer