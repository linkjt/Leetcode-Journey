class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # iterate through the list with all possible values
        for i in range(len(nums)):
            for z in range(i+1, len(nums)):
              # if they equal the target return true
                if nums[i] + nums[z] == target:
                    return i,z
