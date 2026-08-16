# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q = deque([root])
        rightSide = []

        while q:
            rightSide.append(q[-1].val)
            lvlSize = len(q)       

            for i in range(lvlSize):
                top = q.popleft()
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                
        return rightSide
        