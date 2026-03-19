class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrive_time = []

        for d, s in zip(dist, speed):
            arrive_time.append(d / s)
        
        arrive_time.sort()

        res = 0

        for i, a in enumerate(arrive_time):
            
            if i >= a:
                return res
            
            res += 1

        return res

        # res = 0
        # for i in range(len(arrive_time) - 1):
        #     res += 1
        #     if arrive_time[i + 1] - arrive_time[i] <= 1:
        #         return res

        # return res + 1