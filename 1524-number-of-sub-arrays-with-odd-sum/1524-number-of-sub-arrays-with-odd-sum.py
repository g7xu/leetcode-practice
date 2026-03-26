# accumulative sum
# O(1) computation time

# 0 1 4 9

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        event_cnt = 0
        odd_cnt = 0
        res = 0
        cnt = 0
        for i in range(len(arr)):

            cnt += arr[i]

            if cnt % 2 == 0:
                res += odd_cnt
                event_cnt += 1
            else:
                res += 1 + event_cnt
                odd_cnt += 1

        return res % MOD

            
            
