class Solution:
    """
    We traverse the string with a right pointer s while adding each character to a hashmap along with character index.
    if a character exists in hashmap, then we need to increment the left pointer to the next index after that character first appeared.
    At every iteration, we calculate the max length of the window comparing against previous max len and the current window size
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = 0
        max_len = 0

        hmap = {}
        while right<len(s):
            if s[right] in hmap:
                idx = hmap[s[right]]
                if left<=idx:
                    left = idx+1
            max_len = max(max_len, right-left+1)
            hmap[s[right]] = right
            right+=1

        return max_len