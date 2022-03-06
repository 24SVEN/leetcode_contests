import math
class Solution:
    def minimalKSum(self, nums, k: int) -> int:
        #nums.sort()
        # res = []

        # i = 1

        # while len(res) < k:
        #     if i not in nums:
        #         res.append(i)
        #     i += 1


        # return sum(res)

        #dp = [] * k

        res = []
        i=1
        while len(res) < k:
            if i not in nums:
                res.append(i)
            i+=1

        return sum(res)

test = Solution()
print(test.minimalKSum([1,4,25,10,25], 2))
print(test.minimalKSum([5,6], 6))