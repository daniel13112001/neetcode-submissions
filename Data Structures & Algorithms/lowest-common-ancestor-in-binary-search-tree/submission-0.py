# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Traverse the tree from root
If p and q are in the same subtree (i.e both < root), then continue down that subtree
If p and q are in different subtrees, root is the common ancestor
recurse
"""

class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if (p.val >= root.val and q.val <= root.val) or (p.val <= root.val and q.val >= root.val):
            return root
        if p.val <= root.val and q.val <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val >= root.val and q.val >= root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        