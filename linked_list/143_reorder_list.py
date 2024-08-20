# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    We fist find the middle of the list and split the list into two halves. Then we reverse the second half of the list.
    Key is to separate the first and second halves by setting next pointer of prev_slow pointer to None. This avoids infinite loop.
    Then we merge first and seconds halves in alternate manner.
    There is an edge case for even number of nodes. 
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        slow = head
        fast = head
        
        # find the middle of list
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        ## split list into two halves
        prev_slow.next = None
        
        prev = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1 if tmp1 else second
            second = tmp2
        
        return head