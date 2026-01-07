# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        modulo = (10**9)+7
        def treeSum(node):
            if not node:
                return 0
            return node.val + treeSum(node.left) + treeSum(node.right)
        totalSum = treeSum(root)
        maxValue = 0
        def subTreeSum(node):
            nonlocal maxValue
            if not node:
                return 0
            left = subTreeSum(node.left)
            right = subTreeSum(node.right)
            temp = node.val + left + right
            maxValue = max(maxValue,temp*(totalSum-temp))
            return temp
        subTreeSum(root)
        return maxValue % modulo
