from typing import List
import collections
class Solution:
    """
    We want to find the shortest substring in str1 such that str2 is a subsequence of that string.
    A subsequence is a sequence that can be derived from another sequence by deleting zero or more elements without changing the order of the remaining elements.
    We will use the sliding window approach to find an initial solution to the problem (e.g., move through str1 and str2 until str2 is complete)
    Once a solution is found, we need to do a backward search starting from the right pointer to see if we can find a shorter substring
    once backward search is done, we will start the search forward from right_pointer+1 location
    Algorithm terminates when the full str1 string is searched
    Also note that we only store the starting and ending indices of the current minimum substring, so that we don't need to slice strings within loop
    """
    def min_window(self, str1, str2):
        i = 0
        j = 0
        start = 0
        end = len(str1)-1

        min_substr = [0, len(str1)-1]
        min_substr_len = float('infinity')

        while i<len(str1):
            if str1[i]==str2[j]:
                if j==0:
                    start=i
                j+=1
            if j>=len(str2): # solution found. need to do backward search
                end = i
                if end-start+1<min_substr_len:
                    min_substr_len = end-start+1
                    min_substr = [start, end]

                # backward search
                while i>start:
                    j = len(str2)-1
                    if str1[i]==str2[j]:
                        j-=1
                    if j<0: ## found solution in backward search
                        if end - i +1<min_substr_len:
                            min_substr_len=end-i+1
                            min_substr = [i, end]
                    i-=1
                j=0
            i+=1

        return  str1[min_substr[0]: min_substr[1]+1] if min_substr_len<=len(str1) else ""