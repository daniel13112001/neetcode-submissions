# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        numNodes = self._countNodes(root)

        def _goodNodesHelper(root, maxSeen):

            nonlocal numNodes

            if not root:
                return

            if root.val < maxSeen:
                numNodes -= 1
            maxSeen = max(maxSeen, root.val)
            _goodNodesHelper(root.left, maxSeen)
            _goodNodesHelper(root.right, maxSeen)

        _goodNodesHelper(root, float('-inf'))
        return numNodes



    def _countNodes(self, root):
        if not root:
            return 0
        return 1 + self._countNodes(root.left) + self._countNodes(root.right)

        