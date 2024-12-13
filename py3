class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans, marked = 0, [False] * (len(nums)+1)
        for i in sorted(range(len(nums)), key = lambda i: (nums[i], i)):
            if not marked[i]:
                ans += nums[i]
                marked[i-1] = marked[i+1] = True    
        return ans
