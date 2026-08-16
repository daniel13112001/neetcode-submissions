# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from hashlib import sha256

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        collection = set()

        def computeFingerprint(root, collection=None):

            if not root:
                return sha256("null".encode()).hexdigest()
            
            lc = computeFingerprint(root.left, collection)
            rc = computeFingerprint(root.right, collection)

            string = f"{root.val}|{lc}|{rc}"

            m = sha256(string.encode()).hexdigest()

            if collection is not None:
                collection.add(m)

            return m
        
        root = computeFingerprint(root, collection)
        subRoot = computeFingerprint(subRoot)

        return subRoot in collection

        

            
        