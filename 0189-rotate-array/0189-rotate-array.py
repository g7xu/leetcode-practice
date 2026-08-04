class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        k = k % len(nums)

        def helper(s, e, l):
            while s < e:
                l[s], l[e] = l[e], l[s]
                s += 1
                e -= 1

        helper(0, k - 1, nums)
        helper(k, len(nums) - 1, nums)


        