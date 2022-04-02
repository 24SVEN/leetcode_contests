# Input: nums = [1,1,2,3,5]
# Output: 1
# Explanation: You can delete either nums[0] or nums[1] to make nums = [1,2,3,5] which is beautiful. It can be proven you need at least 1 deletion to make nums beautiful.

class Solution:
    def minDeletion(self, nums) -> int:

        num_deleted = 0  
        num_copy = nums.copy()
        counter = 0
        for i in range(len(nums)-1,-1,-1):
            if i < len(nums)-1 and nums[i] == nums[i+1] and i%2 != 0:
                counter += 1
            if i % 2 == 0:
                #if i % 2 == 0,  we need to check if i + 1 is the same
                if i < len(nums)-1 and nums[i] == nums[i+1]:
                    nums.pop(i)
                    num_deleted += 1
                    num_deleted += counter
                    counter = 0
                

        need_to_delete_one = False if len(nums)%2 == 0 else True
        print(nums)
        val = num_deleted + 1 if need_to_delete_one else num_deleted

        #gonna just try popping 1st one
        num_deleted = 1
        num_copy.pop(0)
        counter = 0
        for i in range(len(num_copy)-1,-1,-1):
            if i < len(num_copy)-1 and num_copy[i] == num_copy[i+1] and i%2 != 0:
                counter += 1
            if i % 2 == 0:
                #if i % 2 == 0,  we need to check if i + 1 is the same

                if i < len(num_copy)-1 and num_copy[i] == num_copy[i+1]:
                    num_copy.pop(i)
                    num_deleted += 1
                    num_deleted += counter
                    counter = 0
        need_to_delete_one = False if len(num_copy)%2 == 0 else True
        val2 = num_deleted + 1 if need_to_delete_one else num_deleted

        return min(val,val2)
#[1, 6, 0, 9, 8, 4, 1, 7, 1, 1, 8, 9, 1, 9, ...]
test = Solution()
print(test.minDeletion([1,1,2,3,5])) #1

print(test.minDeletion([1,1,2,2,3,3])) #2

print(test.minDeletion([4,4])) #2

print(test.minDeletion([0,6,6,1,8,7])) #0

# #THERE'S A BETTER WAY THAN MY METHOD. WE NEED MINIMIMUM DELETEIONS
# print(test.minDeletion([1,1,2,2,3,3])) #2

# print(test.minDeletion([8,8,1,3,2,0,1,2,5,0])) #2


print(test.minDeletion([1,6,0,9,8,8,4,1,7,1,1,8,9,1,9,1,2,3,7,6,6,8,7,5,9,7,3,0,4,9,1,8,3,3,2,4,2,6,2,8,9,2,8,4,0,1,0,9,9,5])) #4

#print(test.minDeletion([1, 6, 0, 9, 8, 4, 1, 7, 1, 1, 8, 9, 1, 9, 1, 2, 3, 7, 6, 6, 8, 7, 5, 9, 7, 3, 0, 4, 9, 1, 8, 3, 2, 4, 2, 6, 2, 8, 9, 2, 8, 4, 0, 1, 0, 9, 9, 5]))