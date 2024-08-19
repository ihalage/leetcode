# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    This is a hard problem. We first initialize a dummy node and assign head to dummy.next
    Then, a new variable prev_group_tail is assigned dummy
    Now we iterate while prev_group_tail is not null. We need a new LinkedList named kth_node to find the node after shifting k times
    We find the kth node from current head (which is the next pointer of prev_group_tail) by shifting kth_node k times
    If kth_node does not exists, this is a base case and we return dummy.next

    we want to find the current group head (to reverse it) and current group tail (to link the next part of the LinkedList to it)
    breaking the chain by setting the tail_of_group.next=None is not needed (algorithm will work even if we dont do it)

    then we use a reverse_linked_list_k function to reverse k nodes of our group head. This function should return both head and tail of reversed list
    Then prev_group_tail.next is assigned the reversed_group_head. And reversed_group_tail.next is assigned the next group start (head) 
    Finally we must move the prev_group_tail pointer to the end of the current reversed group (which is the definition of prev_group_tail)

    When the loop terminates, we return dummy.next
    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverses the nodes in a linked list in groups of size k.

        Args:
            head (Optional[ListNode]): The head of the linked list.
            k (int): The size of each group.

        Returns:
            Optional[ListNode]: The head of the modified linked list.

        This function takes a linked list and reverses the nodes in groups of size k. It uses a helper function called `reverse_linked_list_k` to reverse each group of nodes. The function starts by initializing a dummy node and linking it to the head of the linked list. It then iterates through the linked list, finding the start and end of each group of nodes. The nodes in each group are reversed using the `reverse_linked_list_k` function. The function keeps track of the previous group tail and updates it to the end of the current reversed group. Finally, it returns the head of the modified linked list.

        Note:
            - This function assumes that the input linked list is non-empty and that k is a positive integer.

        Example:
            >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
            >>> k = 3
            >>> Solution().reverseKGroup(head, k)
            ListNode(3, ListNode(2, ListNode(1, ListNode(5, ListNode(4))))))

        """
        
        def reverse_linked_list_k(node, k):
            prev, cur = None, node
            for _ in range(k):
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev, node ## need to return reversed_group_head, reversed_group_tail

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy

        while prev_group_tail:
            kth_node = prev_group_tail
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next
                
            cur_group_head = prev_group_tail.next
            next_group_head = kth_node.next

            reversed_group_head, reversed_group_tail = reverse_linked_list_k(cur_group_head, k)
            prev_group_tail.next = reversed_group_head
            reversed_group_tail.next = next_group_head

            # mode prev_group_tail to the tail of the current reversed group
            prev_group_tail = reversed_group_tail

        return dummy.next