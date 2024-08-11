class Solution:
    """
    we want to find the longest substring in string s where all characters are identical after replacing at most k characters in the substring
    to solve this, we keep counting the frequency of each charater in the current window
    We also keep track of what the most frequent character is and its count (max_count)
    The lenght of the window - max_count is the number of replacement we can make as long as this is less than of equal to k
    We keep shifting the left and right pointers under the condition above & update character couts and the max_count
    
    We also update the max_substring length and the max substring (we actually record only the left & right pointer values) to avoid slicing withtin loop
    ^ this is only required if we need to return the max length substring, but in this case we only need to return the length of it. 
    """
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        char_count = {}
        max_count = 0
        max_substr = [0, 0]
        max_len = 0
        while right<len(s):
            if s[right] not in char_count:
                char_count[s[right]] = 1
            else:
                char_count[s[right]] += 1

            if char_count[s[right]]>=max_count:
                max_count=char_count[s[right]]

            if (right-left+1)-max_count<=k:
                if right-left+1>max_len:
                    max_substr = [left, right]
                    max_len = right-left+1
                print(left, right, char_count)
                print(s[max_substr[0]: max_substr[1]+1])
            else:
                char_count[s[left]]-=1
                left+=1
            right+=1
        return max_substr[1] - max_substr[0] + 1 if max_len>0 else 0
