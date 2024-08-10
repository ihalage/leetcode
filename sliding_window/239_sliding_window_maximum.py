from typing import List
import collections
class Solution:
    """
    We want to find the maximum of each contiguous sliding window in linear time
    we will store the INDEX of the maximum value in the current window in a queue. Key here is to store the index of the max value, not the max value itself
    the queue will be updated to to push the new value to the correct location (so that it is sorted in descending order) as the window slides
    if the index of the leftmost value in the queue is outside the current window, it will be removed
    the first value of the queue is appended to the result list (given that at least 1 window has passed) just before sliding the window to the next location
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = collections.deque()

        for i in range(len(nums)):
            if queue and queue[0]<i-k+1: ## max val outside the window
                queue.popleft()
            while queue and nums[queue[-1]]<=nums[i]:
                queue.pop()
            queue.append(i)
            if i>=k-1:
                result.append(nums[queue[0]])
        return result

