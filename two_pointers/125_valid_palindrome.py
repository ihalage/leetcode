class Solution:
    """
    1. remove all alphanumeric characters and make every character lowercase
    2. have two pointers left and right and shift them simultanously checking if they are equal
    3. if not return false
    4. if all corresponding characters are equal then return true
    """
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()] #remove alphanumeric characters
        l, r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True