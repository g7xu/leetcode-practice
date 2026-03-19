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