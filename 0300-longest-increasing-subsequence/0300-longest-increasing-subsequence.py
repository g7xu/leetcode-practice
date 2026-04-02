# pointer

# 

import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []

        for num in nums:
            if not seq or num > seq[-1]:
                seq.append(num)

            idx = bisect.bisect_left(seq, num)
            seq[idx] = num

        return len(seq)