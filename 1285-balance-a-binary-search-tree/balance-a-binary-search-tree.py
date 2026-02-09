class Solution:
    def solve(self, node, vals):
        if not node:
            return
        self.solve(node.left, vals)
        vals.append(node.val)
        self.solve(node.right, vals)
    def tree(self, vals, l, r):
        if l > r:
            return None
        mid  = (l + r) // 2
        node = TreeNode(vals[mid])
        node.left  = self.tree(vals, l, mid - 1)
        node.right = self.tree(vals, mid + 1, r)
        return node
    def balanceBST(self, root):
        vals = []
        self.solve(root, vals)
        return self.tree(vals, 0, len(vals) - 1)