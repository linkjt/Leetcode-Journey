#We can just check the smallest lenght of the string, and we only need to check the first and last alphabetically

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        i = 0
      # We find the minium length that we need to search, via the first and last strings, as they are sorted alphabetically
        min_len = min(len(strs[0]), len(strs[-1]))
      # We check if each of the letters in strings are the same
        while (i<min_len and strs[0][i] == strs[-1][i]):
            i+=1
          # Return True if True
        return strs[0][0:i]


        
