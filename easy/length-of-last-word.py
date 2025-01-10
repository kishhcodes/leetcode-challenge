class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        nums = len(x)
        length = len(x[nums-1])
        return length
