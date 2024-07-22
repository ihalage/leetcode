from typing import List
class Solution:
    """
    1. We first sort nums. this helps in escaping duplicate values and writing an algorithm to use two pointers
    2. iterate nums for the first number (nums[i]). if current number is equal to prev value, we just continue as this leads to duplicates
    3. two pointer algorithm on the remaining portion of the array (e.g., left pointer at i+1 and right pointer at the end)
    4. shift left and right pointers accordingly (if the total sum is greater than 0, we need to shift right pointer to the left and if total is less than 0 we shift left pointer to the right)
    5. if a solution is found, add that to the result
    6. tricky part is to shift pointers when a solution is found. 
        we shift only the left pointer while cur pointer value is equal to its prev value to avoid duplicates.
        no need to shift the right pointer here, because handling of duplicates is taken care of by shifting the left pointer.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return result