class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)

        res = []
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            groups[size].append(i)

            if len(groups[size]) == size:
                res.append(groups[size])
                groups[size] = []

        return res