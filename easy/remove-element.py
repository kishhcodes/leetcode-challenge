class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
                n = len(nums)
                k=0
                index = 0
                for i in range(n):
                    if(nums[i]!=val):
                        nums[index]=nums[i]
                        index += 1
                        k += 1
                return k
