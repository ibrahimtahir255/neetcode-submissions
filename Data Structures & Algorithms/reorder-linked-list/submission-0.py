# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find the middle of the list using slow/fast pointers 
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half_head = slow.next
        slow.next = None

        # reverse the second half
        reversed_list = self.reverse_list(second_half_head)

        # merge the two halves
        return self.merge_two_lists(head, reversed_list)

    def reverse_list(self, head):
        curr = head
        prev = None

        while curr:
            # save next node
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def merge_two_lists(self, list1, list2):
        while list1 and list2:
            next1 = list1.next  
            next2 = list2.next  
            list1.next = list2   
            list2.next = next1  
            list1 = next1
            list2 = next2


        
    