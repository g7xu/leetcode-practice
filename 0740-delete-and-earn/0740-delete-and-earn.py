class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        num_points = sorted((num, num * counter[num]) for num in set(nums))

        @cache
        def helper(i):
            if i >= len(num_points):
                return 0

            val, pts = num_points[i]

            # find next non-adjacent value index
            skip = i + 1
            if skip < len(num_points) and num_points[skip][0] == val + 1:
                skip += 1

            take = pts + helper(skip)
            dont_take = helper(i + 1)

            return max(take, dont_take)

        return helper(0)