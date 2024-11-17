# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root, height):
            if not root:
                return None
            
            if len(res) == height:
                res.append(root.val)
            
            dfs(root.right, height + 1)
            dfs(root.left, height + 1)
        
        dfs(root, 0)
        return res
