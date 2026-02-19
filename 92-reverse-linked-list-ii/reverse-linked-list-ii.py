# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # 1. Reach the node just before the 'left' position
        # We use a dummy node to handle cases where left = 1
        dummy = ListNode(0, head)
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        # 2. Start the reversal process
        # 'cur' is the node that will eventually be at the end of the reversed section
        cur = prev.next
        
        for _ in range(right - left):
            # 'temp' is the node we are moving to the front of the reversed section
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next