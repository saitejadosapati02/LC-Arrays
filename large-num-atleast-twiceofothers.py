class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        max_ind = nums.index(max_num)
        
        for i in range(len(nums)):
            if i != max_ind and max_num < 2 * nums[i]:
                return -1
                
        return max_ind