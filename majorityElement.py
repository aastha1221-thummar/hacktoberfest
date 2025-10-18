class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

def _driver():
    param_1 = [3,2,3]
    ret = Solution().majorityElement(param_1)
    print(ret)

_driver()
