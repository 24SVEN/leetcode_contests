class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        r = []
        for i in range(len(a)):
            if len(r) % 2 == 0 or a[i] != r[-1]:
                r.append(a[i])
        if len(r) % 2:
            r.pop()
        return len(a) - len(r)

test = Solution()
print(test.minDeletion([1,1,2,3,5])) #1

print(test.minDeletion([1,1,2,2,3,3])) #2

print(test.minDeletion([4,4])) #2

print(test.minDeletion([0,6,6,1,8,7])) #0

print(test.minDeletion([1,6,0,9,8,8,4,1,7,1,1,8,9,1,9,1,2,3,7,6,6,8,7,5,9,7,3,0,4,9,1,8,3,3,2,4,2,6,2,8,9,2,8,4,0,1,0,9,9,5])) #4