class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp=[[0] * k for _ in range(k)]
        maxlen=0
        for num in nums:
            current_rem=num%k
            for prev_rem in range(k):
                dp[prev_rem][current_rem]=dp[current_rem][prev_rem]+1
                maxlen=max(maxlen, dp[prev_rem][current_rem])
        return maxlen
        