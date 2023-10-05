# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        hare = head
        tortoise = head
        prev = None

        while hare and hare.next:
            hare = hare.next.next
            prev = tortoise
            tortoise = tortoise.next

        prev.next = tortoise.next
        return head
