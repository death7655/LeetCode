from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = Counter(nums)
        output = []
        for key, value in duplicates.items():
            if value > 1:
                output.append(key)
        return output
        