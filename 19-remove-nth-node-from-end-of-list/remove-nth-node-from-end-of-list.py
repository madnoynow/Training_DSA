# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Using a dummy node simplifies edge cases like removing the head
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # 1. Advance fast pointer so that there is a gap of n nodes between fast and slow
        for _ in range(n + 1):
            fast = fast.next
            
        # 2. Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
            
        # 3. Skip the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next