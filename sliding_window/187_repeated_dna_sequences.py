from typing import List
class Solution:
    """
    We will be using a rolling polynomial hash with a sliding window approach to detect repeated substrings.
    We first need to map every unique charater in the string to a numeric value. In DNA sequences we have (a=4) unique characters {A:1, C:2, G:3, T:4}
    Let's say k is the substring length.
    We then need to define a polynomial hash function -> c1*a^(k-1)+c2*a^(k-2)+..+cka^(0)
    We will calculate the hash value of the substring in the window H(w) as we move forward
    Key thing to note, how the first character is removed and the incoming character is added, and how the hash value is updated for current window as we slide
    For eg., S = "ATGCAGTC" and k=3, H(ATG) = 1*4^(2)+4*4^(1)+3*4^(0) = 35. Then we remove A and add C and update hash value of window as follows.
    H(TGC) = [H(ATG) - H(A)]*4+H(C). Note multiplying by 4 to adjust the place. Because we moved to right, T is our new first character, so we're shifting everything to left by multiplying with `a`
    If this hash value is in the hashset, we add the substring to the result. Else we add the hashvalue to hashset and continue sliding window.
    """
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mapping = {'A':1, 'C':2, 'G':3, 'T':4}
        a=4
        k=10
        left = 0

        # corner case when the length of the string is less than the window
        if len(s)<k:
            return []

        hashset = set({})
        resultset = set({})

        hashval = 0
        for i in range(k):
            hashval+=mapping[s[i]]*(a**(k-(i+1)))
        hashset.add(hashval)

        while left+k<len(s):
            left+=1
            hashval = (hashval-mapping[s[left-1]]*(a**(k-1)))*a + mapping[s[left+k-1]]*(a**(0))
            if hashval in hashset and s[left:left+k] not in resultset:
                resultset.add(s[left:left+k])
            else:
                hashset.add(hashval)

        return list(resultset)

