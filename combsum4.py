class Solution:
    def getCombinationSum(self, candidates, res, target, index, combination):
        if target == 0:
            res.append(combination)
            return
        
        if target < 0:
            return
        
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            self.getCombinationSum(candidates, res, target-candidates[i], 0, combination+[candidates[i]])
        
    def combinationSum4(self, candidates, target):
        candidates.sort()
        res = []
        combination = []
        self.getCombinationSum(candidates, res, target, 0, combination)
        return len(res)
        
c = Solution()
c.combinationSum4([4,2,1], 32)
        