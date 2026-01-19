# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        s = []
        result = []
        while root or s:
            while root:
                s.append(root)
                root = root.left
            root=s.pop()
            result.append(root.val)
            root = root.right
        return result