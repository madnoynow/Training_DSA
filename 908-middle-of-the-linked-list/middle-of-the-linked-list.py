# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head):
        sp = head
        fp = head
        
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        
        return sp
