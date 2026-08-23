# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        path = []

        def bst(root):

            if not root:
                return 
            
            bst(root.left)
            path.append(root.val)
            bst(root.right)
            
        
        bst(root)
        
        for i in range(1, len(path)):
            if path[i] <= path[i-1]:
                return False 

        return True

        
        