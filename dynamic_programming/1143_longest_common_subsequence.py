class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Treat this as a 2D DP problem. text1 characters are in rows (i) and text2 chars are in columns (j).
        if text1[i]==text2[j] then we do dp[i][j]=dp[i+1][j+1]+1
        Else we have two cases, we leave out one char in text1 and run dp on text2 and text1[i+1:]
        or we leave out one char in text2 and do dp on text2[j+1:] and text1
        '''
        dp = [[0 for i in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i]==text2[j]:
                    dp[i][j]=1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        # print(dp)
        return dp[0][0]
