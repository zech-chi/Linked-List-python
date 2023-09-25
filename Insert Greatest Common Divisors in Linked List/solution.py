# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        def gcd(x, y):
            for m in range(min(x, y), 1, -1):
                if x % m == 0 and y % m == 0:
                    return m
            return 1
        
        cur_node = head
        while cur_node.next:
            next_node = cur_node.next
            GCD = gcd(cur_node.val, next_node.val)
            new_node = ListNode(GCD, next_node)
            cur_node.next = new_node
            cur_node = cur_node.next.next

        return head 
