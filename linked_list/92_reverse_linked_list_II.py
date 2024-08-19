# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Brute force approach would be to detach the sublist from the original linked list, reverse the sublit and reattach it back.
    In the optimized approach coded below, we reverse the sublist in place.
    Our prev pointer should be one node behind left. cur pointer is initialized at the left node.
    The key here is to detach next_node = cur.next node by setting cur.next to the next_node.next and
    point next_node.next to prev.next and prev.next to the next_node so that next_node is brought in front of
    the sublist after reversing. Think of it as at every iteration, the last node (cur.next) is brought to the front
    as the next node of prev. Note that prev remains unchanged at one node behind the left node.
    It would be helpful to draw this on paper to see how the links are broken and recreated.
    """
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left-1):
            prev = prev.next

        cur = prev.next
        for _ in range(right-left):
            next_node = cur.next
            cur.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
        

