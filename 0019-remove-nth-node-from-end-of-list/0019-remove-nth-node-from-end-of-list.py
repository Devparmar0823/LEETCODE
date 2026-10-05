# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        size=0
        temp=head
        while temp:
            temp=temp.next
            size+=1
        dummy = ListNode(0)
        dummy.next = head
        temp1 = dummy
        for _ in range(size - n):
            temp1 = temp1.next
        temp1.next = temp1.next.next
        return dummy.next