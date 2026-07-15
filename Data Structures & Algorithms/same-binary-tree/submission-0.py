# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # base cases
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        if p.val == q.val:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
        else:
            return False

        if left == False or right == False:
            return False
        if left == True or right == True:
            return True
