class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            unique_pos = 0
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    nums[unique_pos] = nums[i]  
                    unique_pos += 1

            for j in range(unique_pos, len(nums)):
                nums[j] = '_'

            return unique_pos
