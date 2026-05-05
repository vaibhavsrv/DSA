# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        current = head

        while current.next:
            length += 1
            current = current.next

        k = k % length
        if k == 0:
            return head
        
        tail = head
        for _ in range(length - k - 1):
            tail = tail.next

        new = tail.next
        tail.next = None
        current.next = head

        return new