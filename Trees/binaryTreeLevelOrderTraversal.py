# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def traverse(root, height):
            if not root:
                return

            if len(res) == height:
                res.append([root.val])
            else:
                res[height].append(root.val)
            
            traverse(root.left, height + 1)
            traverse(root.right, height + 1)
        
        traverse(root, 0)
        return res
