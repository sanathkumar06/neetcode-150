class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for index, item in enumerate(nums):
            if item in lookup.keys():
                return [lookup[item], index]
            else:
                lookup[target - item] = index
        return []
