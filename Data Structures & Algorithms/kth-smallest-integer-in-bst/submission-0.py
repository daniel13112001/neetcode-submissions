# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        ans = None

        def counter(root):

            nonlocal count, ans 

            if not root:
                return
            
            counter(root.left)

            count += 1
            if count == k:
                ans = root.val
                return
            
            counter(root.right)

        counter(root)
        return ans
        