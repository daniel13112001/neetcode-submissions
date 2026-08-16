# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = deque([(root, 0)])
        ans = [(root, 0)]
        ret = [[]]

        [(1,0), (2,1), (3,1), (4,2), (5,2), (6,2), (7,2)]

        while q:
            cur, lvl = q.popleft()
            if cur.left:
                q.append((cur.left, lvl+1))
                ans.append((cur.left, lvl+1))
            if cur.right:
                q.append((cur.right, lvl+1))
                ans.append((cur.right, lvl+1))

        curlvl = 0
        for node, lvl in ans:
            if lvl == curlvl:
                ret[curlvl].append(node.val)
            else:
                ret.append([node.val])
                curlvl = lvl
        return ret



        