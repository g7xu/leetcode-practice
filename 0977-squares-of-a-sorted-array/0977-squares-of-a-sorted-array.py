# brute force
# square every element
# sort the list
# O(n log n)

# use the two pointer idea
# find the smallest negative and smallest positive
# keep expand to left and right depending on the size

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        # find starting point
        p = 0
        while p < len(nums):
            if nums[p] >= 0:
                break
            p += 1

        # no negative
        if p == 0:
            return [i ** 2 for i in nums]
        
        # no positive
        if p == len(nums):
            return [i ** 2 for i in nums][::-1]

        pos = p
        neg = p - 1

        res = []
        while pos < len(nums) or neg >= 0:
            if pos >= len(nums):
                res.append(nums[neg] ** 2)
                neg -= 1
                continue

            if neg < 0:
                res.append(nums[pos] ** 2)
                pos += 1
                continue

            if abs(nums[neg]) < nums[pos]:
                res.append(nums[neg] ** 2)
                neg -= 1
            else:
                res.append(nums[pos] ** 2)
                pos += 1

        return res
                
