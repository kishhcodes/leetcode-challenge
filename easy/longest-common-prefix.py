class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = [x.lower() for x in strs]
        min_len = min(len(s) for s in x)
        res = ""

        for j in range(min_len):
            if all(x[i][j] == x[0][j] for i in range(len(x))):
               res += x[0][j] 
            else:
                break
        
        return res
