class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        e = set()

        for st, en in paths:
            s.add(st)
            e.add(en)

        for ele in e:
            if ele not in s:
                return ele