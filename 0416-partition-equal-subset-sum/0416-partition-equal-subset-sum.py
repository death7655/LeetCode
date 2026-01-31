class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target_sum = total//2
        n = len(nums)

        dp = {0}
        for num in nums:
            next_dp = set(dp)
            for s in dp:
                current_sum = s + num
                if current_sum == target_sum:
                    return True
                if current_sum < target_sum:
                    next_dp.add(current_sum)
                dp = next_dp
        return False