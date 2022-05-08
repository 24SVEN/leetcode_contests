class Solution:
    def intersection(self, nums):
        hashmap = {}

        for li in nums:
            for num in li:
                hashmap[num] = hashmap.get(num,0) + 1

        result = []
        for key,val in hashmap.items():
            if val == len(nums):
                result.append(key)


        return sorted(result)


