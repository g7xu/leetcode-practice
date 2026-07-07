# helper(text):
    # process each part
    # and the for things in %%,
    # mapping and call recurisve func

    # return complete string

class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mapping = dict()
        for k, v in replacements:
            mapping[k] = v

        @cache
        def helper(text):
            res = ''
            p = 0
            while p < len(text):
                if text[p] == '%':
                    res += helper(mapping[text[p+1]])
                    p += 2
                else:
                    res += text[p]
                p += 1

            return res

        return helper(text)