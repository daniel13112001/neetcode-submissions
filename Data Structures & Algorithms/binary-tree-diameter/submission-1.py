# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def diameterHelper(root):

            nonlocal diameter

            if not root:
                return 0

            left = self.height(root.left)
            right = self.height(root.right)

            diameter = max(diameter, left+right)
            

            diameterHelper(root.left)
            diameterHelper(root.right)

        diameterHelper(root)
        return diameter

        


        