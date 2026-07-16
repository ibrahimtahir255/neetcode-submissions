# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        # if root.val == subRoot.val:
        #     return True

        def isSameTree(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False

            if p.val == q.val:
                left = isSameTree(p.left, q.left)
                right = isSameTree(p.right, q.right)
            else:
                return False
            
            if left == False and right == False:
                return False
            if left == True and right == True:
                return True
        
        node_tree = isSameTree(root, subRoot)
        left_tree = self.isSubtree(root.left, subRoot)
        right_tree = self.isSubtree(root.right, subRoot)

        if left_tree or right_tree or node_tree:
            return True
        else:
            return False
        
        