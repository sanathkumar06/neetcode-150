class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        ans = []
        li = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n not in res:
                res[n] = 1
            else:
                res[n] += 1

        for key, val in res.items():
            li[val].append(key)
            
        for i in reversed(li):
            for num in i:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
