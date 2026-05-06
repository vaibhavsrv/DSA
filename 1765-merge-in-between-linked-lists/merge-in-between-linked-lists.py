# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp =list1
        count = 0

        while count < a - 1:
            temp = temp.next
            count +=1

        first = temp

        while count < b:
            temp = temp.next
            count += 1

        second = temp.next
        first.next = list2

        temp2 = list2

        while temp2.next:
            temp2 = temp2.next

        temp2.next = second
        return list1