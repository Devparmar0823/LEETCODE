# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        nums=[]
        temp=head
        while temp:
            nums.append(temp.val)
            temp=temp.next
        if nums==nums[::-1]:
            return True
        return False