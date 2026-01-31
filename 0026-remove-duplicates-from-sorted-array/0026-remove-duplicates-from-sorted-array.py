from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        
        for key, value in counts.items():
            count = value - 1
            for i in range(count):
                nums.remove(key)
        return len(nums)
        
        