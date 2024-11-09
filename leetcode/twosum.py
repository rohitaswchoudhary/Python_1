nums = [2, 7, 11,15]
target = 9

class Solution (object):
    def twoSum(self, nums, target):
        mapping = {}

        for index, val in enumerate(nums):
            diff = target - val
            if diff in mapping:
                return[index, mapping[diff]]
            else:
                mapping[val]= index

print(Solution.twoSum(self,nums,target))