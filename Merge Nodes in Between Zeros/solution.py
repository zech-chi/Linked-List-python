# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_ans = ListNode()
        cur_node_ans = head_ans
        cur_node = head
        while cur_node:
            cur_node = cur_node.next
            if not cur_node:
                break
            
            new_node_ans = ListNode()
            while cur_node.val != 0:
                new_node_ans.val += cur_node.val
                cur_node = cur_node.next
            
            if cur_node_ans == None:
                cur_node_ans = new_node_ans
            else:
                cur_node_ans.next = new_node_ans
                cur_node_ans = cur_node_ans.next
        
        return head_ans.next
