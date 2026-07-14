# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # # traverse the list once so we can get the length
        # curr = head
        # length = 0
        # while curr:
        #     length += 1
        #     curr = curr.next
    
        # # find the node to be removed
        # node_index = length - n
        # count = 0
        
        # # second traverse for removal
        # curr = head
        # prev = head
        # while curr and count != node_index:
        #     count += 1
        #     prev = curr
        #     curr = curr.next
            
        # # accoutn for edge case where the node to remove is the head
        # if node_index == 0:
        #     return head.next
        
        # else:
        #     prev.next = prev.next.next
        #     return head


        dummy = ListNode()
        dummy.next = head

        left = dummy
        right = head

        for _ in range (n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
        
        
            

        