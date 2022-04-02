class Solution:
    def triangularSum(self, nums) -> int:
        if len(nums) == 0:
            return 0
        while len(nums) > 1:
            merged = []
            for i in range(1,len(nums)):
                merged.append((nums[i] + nums[i-1]) % 10)
            nums = merged

        return nums[0]


test = Solution()
print(test.triangularSum([1,2,3,4,5]))
print(test.triangularSum([5]))