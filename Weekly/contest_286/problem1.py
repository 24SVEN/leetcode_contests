# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].


class Solution:
    def findDifference(self, nums1, nums2):
        hashmap_1 = {}
        hashmap_2 = {}

        answers1,answers2 = set(),set()

        for num in nums1:
            hashmap_1[num] = 1 + hashmap_1.get(num,0)

        for num in nums2:
            hashmap_2[num] = 1 + hashmap_2.get(num,0)


        for num in nums1:
            if num not in hashmap_2:
                answers1.add(num)

        for num in nums2:
            if num not in hashmap_1:
                answers2.add(num)

        return [list(answers1),list(answers2)]

test = Solution()
print(test.findDifference([1,2,3],[2,4,6]))
print(test.findDifference([1,2,3,3],[1,1,2,2]))

