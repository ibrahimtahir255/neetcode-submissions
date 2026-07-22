from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do a breadth first search and add nodes to a list of list by levels

        if not root:
            return []

        # initialize a queue
        queue = deque()

        # add the root to queue
        queue.append(root)

        # initialize a list
        out_list = []

        final_list= []

        # while queue is not empty
        while queue:
            level_size = len(queue)
            level = []
            # for the length of level_size
            for i in range (level_size):
                # pop the node at the front
                node = queue.popleft()
                # append to level
                level.append(node.val)

                if node.left:
                    # add node.left to queue
                    queue.append(node.left)
                if node.right:
                    # add node.right to queue
                    queue.append(node.right)

            final_list.append(level[-1])
            
        return final_list



        