import heapq
class Solution:
    def maximumProduct(self, nums, k: int) -> int:
        heapq.heapify(nums)

        while k > 0:
            num = heapq.heappop(nums)
            heapq.heappush(nums,num + 1)

            k-= 1
        
        answer = 1
        for i in range(len(nums)):
            answer = (nums[i] * answer) % (10**9 + 7)

        return answer


test = Solution()
print(test.maximumProduct([0,4],5))