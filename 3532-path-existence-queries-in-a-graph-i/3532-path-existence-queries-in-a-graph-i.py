class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # max_idx = [i for i in range(n)]

        # s = 0
        # for i in range(n):
        #     if i != len(nums) and nums[i + 1] - nums[i] <= maxDiff:

        root = [i for i in range(n)]

        start = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                root[i] = start
            else:
                start = i 

        res = []
        for a, b in queries:
            res.append(root[a] == root[b])
        return res




        # max_idx = dict()

        # slow = fast = 0
        # while fast < len(nums):

        #     if fast == len(nums) - 1 or abs(nums[fast + 1] - nums[fast]) > maxDiff:
        #         while slow <= fast:
        #             max_idx[slow] = fast
        #             slow += 1

        #         fast += 1
        #         continue

        #     fast += 1

        # res = []
        # for q in queries:
        #     a, b = sorted(q)
        #     if max_idx[a] >= b:
        #         res.append(True)
        #     else:
        #         res.append(False)

        # return res 
