# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Key idea is the shift the pointer until it reaches the end of list. When that happens, the pointer will be switched to the head of the otherr list.
        Same goes for both pointers.
        In the next iteration, two pointers should meet if there is an intersection, if not they both will reach the end at the same time, and None will be returned.
        Key here is if the length of two lists are A, and B., we do another iteration to travel the same length A+B = B+A
        """
        pointer1, pointer2 = headA, headB

        while pointer1!=pointer2:
            if pointer1:
                pointer1 = pointer1.next
            else: ## reached the end of it so switch to the head of other list
                pointer1 = headB
            
            if pointer2:
                pointer2 = pointer2.next
            else:
                pointer2 = headA

        return pointer1



        