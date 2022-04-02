#6027

class Solution:
    def countHillValley(self, nums: list[int]) -> int:


        #1 for going up, 0 for neutral, -1 for down
        going_up = 0
        count = 0

        #add for valley or hill whenever direction change
        for i in range(0,len(nums)-1):
            if nums[i+1] > nums[i] and going_up == 0:
                going_up = 1
            elif nums[i+1] >= nums[i] and going_up == 1:
                pass
            elif nums[i+1] > nums[i] and going_up == -1:
                going_up = 1
                count +=1

            elif nums[i+1] < nums[i] and going_up == 0:
                going_up = -1
            elif nums[i+1] <= nums[i] and going_up == -1:
                pass
            elif nums[i+1] < nums[i] and going_up == 1:
                going_up = -1
                count +=1
            
        return count



test = Solution()
#print(test.countHillValley([2,4,1,1,6,5]))
#print(test.countHillValley([6,6,5,5,4,1]))
print(test.countHillValley([1]))