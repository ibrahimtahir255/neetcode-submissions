from collections import deque
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

        # intialize a queue
        queue = deque()

        # intialize a list to return
        visited_nodes = []
    

        # add root to queue
        queue.append(root)

        # while the queue is not empty
        while queue:
            level_size = len(queue)
            level = []

            # for loop till length of the queue
            for i in range(level_size):
                node = queue.popleft()

                # append to level list 
                level.append(node.val)

                # add the next node's left child to queue 
                if node.left:
                    queue.append(node.left)

                # add the next node's right child to queue 
                if node.right:
                    queue.append(node.right)


            # append level list ot final lsit
            visited_nodes.append(level)
            
          
        return visited_nodes
