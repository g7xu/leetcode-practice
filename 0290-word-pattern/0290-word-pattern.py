class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        mapping = dict()
        reverse_mapping = dict()

        plist = list(pattern)
        slist = s.split(' ')

        if len(plist) != len(slist):
            return False

        for k, v in zip(plist, slist):
            if k in mapping:
                if mapping[k] != v:
                    return False
            else:
                mapping[k] = v

            if v in reverse_mapping:
                if reverse_mapping[v] != k:
                    return False
            else:
                reverse_mapping[v] =k

        return True