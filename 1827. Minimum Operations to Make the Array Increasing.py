class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                cnt += nums[i] - nums[i + 1] + 1
                nums[i + 1] += nums[i] - nums[i + 1] + 1
        # print(cnt)
        return cnt