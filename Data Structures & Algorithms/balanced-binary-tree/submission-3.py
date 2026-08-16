# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True


        def heightAndBalance(root):

            if not root:
                return (True, 0)

            lcb, lch = heightAndBalance(root.left)
            rcb, rch = heightAndBalance(root.right)

            if not lcb or not rcb:
                return (False, -1)

            if abs(lch-rch) > 1:
                return (False, -1)

            return (True, 1+max(lch, rch))

        return heightAndBalance(root)[0]
        