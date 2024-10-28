class Solution:
    def isPalindrome(self, x: int) -> bool:
      # All Negatives Are False
        if x<0:
            return False
        res = list(map(int, str(x)))
      # iterate through the list, checking that indexs are equal to their corasponding indexs over the haf 
        for i in range(len(res)//2):
            if res[i] != res[-(1+i)]:
                return False
        return True
