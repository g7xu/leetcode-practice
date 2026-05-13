# choose nothing
# choose one from the dictionary

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)

        def helper():
            res = 1
            
            for kind, c in freq.items():
                if c == 0:
                    continue

                freq[kind] -= 1
                res += helper()
                freq[kind] += 1

            return res

        return helper() - 1
            
