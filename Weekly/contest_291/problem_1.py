class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        #sort then use as stack
        
        max_digit = 0        
        nums = [char for char in number]

        for i in range(len(nums)):
            #rebuild at every removal
            if nums[i] == digit:

                #temp compy
                temp = nums.copy()
                temp.pop(i)
                temp_int = int("".join(temp))
                max_digit = max(max_digit,temp_int)
                
        return str(max_digit)


test = Solution()
print(test.removeDigit("123","3"))
print(test.removeDigit("1231","1"))

print(test.removeDigit("551","5"))

