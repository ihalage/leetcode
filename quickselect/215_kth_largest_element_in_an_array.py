import random
class Solution:
    """
    Uses the quickselect algorith. Selects a pivot randomly and put elements greater than the pivot to the left,
    equal to the pivot to the middle and less than the pivot to the right. Then recursively localize the kth largest 
    element by searching in the correct subarray.
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
