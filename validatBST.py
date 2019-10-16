# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):


        def helper(node, left=float('-inf'), right=float('inf')):
            if not node:
                return True
            val= node.val
            if val <= left or val >= right:
                return False
            if not helper(node.left, left, val):
                return False
            if not helper(node.right, val, right):
                return False
            return True
        return helper(root)



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right =TreeNode(3)
print(Solution().isValidBST(root))
