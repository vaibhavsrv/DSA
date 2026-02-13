# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = []
        depth = 1
        queue.append((root,depth))
        while queue:
            current,d = queue.pop(0)
            if current.left is None and current.right is None:
                return d
            if current.left:
                queue.append((current.left,d+1))
            if current.right:
                queue.append((current.right,d+1))
        return depth