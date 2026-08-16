# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def _goodNodesHelper(root, maxSeen):

            if not root:
                return 0
            
            if root.val >= maxSeen:
                good = 1
            else:
                good = 0

            maxSeen = max(root.val, maxSeen)
            
            return good + _goodNodesHelper(root.left, maxSeen) + _goodNodesHelper(root.right, maxSeen)

        return _goodNodesHelper(root, float('-inf'))