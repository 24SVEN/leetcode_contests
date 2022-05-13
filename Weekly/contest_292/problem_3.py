class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        dp = [1 for i in range(len(pressedKeys))]


        same_char_count = 1
        var = 1
        #need to make a case exception for first
        for i in range(1,len(pressedKeys)):
            n1,n2 = pressedKeys[i],pressedKeys[i-1]

            if n1 == n2:
                same_char_count += 1
                var *= 2

                dp[i] = dp[i-same_char_count + 1] * var

            else:
                var = 1
                same_char_count = 1
                dp[i] = dp[i-1]
            
        return dp[-1] % (10 ** 9 + 7)



test = Solution()
#print(test.countTexts("22233"))
print(test.countTexts("222222222222222222222222222222222222"))