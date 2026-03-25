class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        visited = set()

        @cache
        def helper(p, nums, visited):
            if p >= len(nums):
                return 0

            cand = []
            # pick
            if nums[p] + 1 not in visited and nums[p] - 1 not in visited:
                visited = set(visited)
                visited.add(nums[p])
                cand.append(count[nums[p]] * nums[p] + helper(p + 1, nums, frozenset(visited)))
                visited.remove(nums[p])

            # not pick
            cand.append(helper(p + 1, nums, frozenset(visited)))

            return max(cand)

        nums = tuple(set(nums))
        return helper(0, nums, frozenset(visited))