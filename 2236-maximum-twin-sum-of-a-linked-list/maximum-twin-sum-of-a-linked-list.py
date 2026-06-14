# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        newLinkedList = []
        current = head
        while current:
            newLinkedList.append(current.val)
            current = current.next

        n = len(newLinkedList)
        max_sum = 0
        for i in range(n//2):
            max_sum = max(max_sum,newLinkedList[i] + newLinkedList[n-1-i])


        return max_sum