class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        chars = set({str(i) for i in range(1, 27)})
        dp = [0]*(len(s)+1)
        dp[0] = 1 ## for empty string, we want to return 1
        dp[1] = 1

        for i in range(2, len(s)+1):
            if s[i-2:i] in chars:
                dp[i] = dp[i]+dp[i-2]
            if s[i-1] in chars:
                dp[i] = dp[i]+dp[i-1]

        # print(dp)
        return dp[-1]